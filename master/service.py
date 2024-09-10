from concurrent import futures
from enum import Enum
import queue
import threading
import time
from typing import Dict, List, Optional
import uuid

import grpc

from gen import service_pb2 as A
from gen import service_pb2_grpc as B
import utils


worker_heartbeat_dict: utils.ExpiringDict = utils.ExpiringDict()
# 任务执行的阶段


class jobStatus(Enum):
    WAITING = "waiting"
    MAPPING = "mapping"
    REDUCING = "reducing"
    FINISH = "finished"
    FAILED = "failed"


class taskStatus(Enum):
    WAITING = "waiting"  # 还没加入队列
    QUEUE = "queue"  # 在队列中
    DOING = "doing"  # 已经分配给worker
    FINISH = "finished"  # 顺利结束
    FAILED = "failed"  # 执行失败


class taskType(Enum):
    MAP = "map"
    REDUCE = "reduce"


class serverAddress:
    def __init__(self, ip: str, port: int):
        self.ip: str = ip
        self.port: int = port

    def identity(self):
        return f"{self.ip}:{self.port}"


class filePath:
    def __init__(self, server: serverAddress, path: str, task=None):
        self.serverAddress: serverAddress = server
        self.path: str = path
        # 记录由哪个任务产生, 当文件获取失败时,重新执行之间的任务
        self.generated_by_task: Optional[Task] = task


class Task:
    def __init__(self, job_id: str, task_type: taskType, task_index: int, file_path: List[filePath]):
        self.job_id: str = job_id
        self.task_id: int = task_index
        self.task_type: taskType = task_type
        self.file_path: List[filePath] = file_path


class taskProgress():
    def __init__(self, job_id: str, task_type: taskType, task_index: int, interval: int = 10):
        self.job_id: str = job_id
        self.task_type: taskType = task_type
        self.task_index: int = task_index
        self.task_status: taskStatus = taskStatus.WAITING
        self.task_allocation_time: None | int = None
        self.worker: serverAddress | None = None
        self.query_interval: int = interval

    def cancel(self) -> None:
        self.task_status = taskStatus.WAITING
        self.task_allocation_time = None
        self.worker = None

    def re_put_task_to_queue(self) -> None:
        if self.task_type == taskType.MAP:
            job = JOB_DICT[self.job_id]
            task = Task(
                job_id=self.job_id,
                task_type=self.task_type,
                task_index=self.task_index,
                file_path=[job.file_for_map[self.task_index]]
            )
            taskQueue.put(task)
        else:
            job = JOB_DICT[self.job_id]
            file_for_reduce = [x[self.task_index] for x in job.file_for_reduce]
            task = Task(
                job_id=self.job_id,
                task_type=self.task_type,
                task_index=self.task_index,
                file_path=file_for_reduce
            )

    def check_worker_alive(self) -> bool:
        assert self.worker != None
        if worker_heartbeat_dict.get(self.worker.identity()) == None:
            return False
        return True

    def check_worker_alive_loop(self) -> None:
        while True:
            if self.task_type == taskType.MAP:
                if self.task_status == taskStatus.WAITING or self.task_status == taskStatus.QUEUE:
                    time.sleep(1)
                    pass

                elif self.task_status == taskStatus.FINISH:
                    return

                assert self.task_status == taskStatus.DOING
                assert self.worker != None, "DOING 状态一定分配了worker"
                if not self.check_worker_alive():
                    self.task_status = taskStatus.WAITING
                    self.task_allocation_time = None
                    self.worker = None
                    # TODO: Log
                    self.re_put_task_to_queue()
                time.sleep(self.query_interval)


class Job:
    def __init__(self, request: A.UploadJobRequest, job_id: str):
        self.lock = threading.Lock()  # 添加锁以避免竞争条件
        self.job_id: str = job_id
        self.map_num: int = request.mapNum
        self.reduce_num: int = request.reduceNum
        self.job_upload_time: int = int(time.time())
        self.client_server_address: serverAddress = serverAddress(
            ip=request.serverAddress.ip,
            port=request.serverAddress.port,
        )
        self.map_reduce_func_path: filePath = filePath(
            server=self.client_server_address,
            path=request.mapReduceFuncPath.path,
        )
        self.file_for_map: List[filePath] = [
            filePath(server=self.client_server_address, path=path.path)
            for path in request.filePaths]
        self.file_for_reduce: List[List[filePath]] = [[]
                                                      for _ in range(request.mapNum)]
        self.status: jobStatus = jobStatus.WAITING
        self.map_task_progress: List[taskProgress] = [
            taskProgress(job_id=job_id, task_type=taskType.MAP, task_index=i)
            for i in range(request.mapNum)
        ]
        self.reduce_task_progress: List[taskProgress] = [
            taskProgress(
                job_id=job_id, task_type=taskType.REDUCE, task_index=i)
            for i in range(request.reduceNum)
        ]

    def some_method(self):  # 示例方法，示范如何使用锁
        with self.lock:
            # 进行线程安全操作
            pass


        # 记录正在执行的任务
JOB_DICT: Dict[str, Job] = dict()

# job队列
jobQueue = queue.Queue()
# task队列,由job拆分得到
taskQueue = queue.Queue()
# 空闲worker队列
workerQueue = queue.Queue()


def generate_map_task_from_Queue():
    """
    生成map task
    将job队列中的任务取出，并拆分成map task
    """
    while True:
        job: Job = jobQueue.get()
        with job.lock:
            if job.status != jobStatus.WAITING:
                raise RuntimeError(
                    f"gnerate_map_task: job: {job.job_id} status is not waiting")
            for i in range(job.map_num):
                map_task = Task(job_id=job.job_id, task_type=taskType.MAP,
                                task_index=i, file_path=[job.file_for_map[i]])
                taskQueue.put(map_task)
                job.map_task_progress[i] = taskProgress(
                    job_id=job.job_id,
                    task_type=taskType.MAP,
                    task_index=i,
                )
            job.status = jobStatus.MAPPING


class MasterServicer(B.MasterServicer):
    def UploadJob(self, request: A.UploadJobRequest, context: grpc.ServicerContext) -> A.UploadJobResponse:
        for path in request.filePaths:
            print(path.path)
        # 产生唯一ID
        jobID = str(uuid.uuid4())
        job = Job(request, jobID)
        JOB_DICT[jobID] = job
        # 加入job队列
        jobQueue.put(job)
        return A.UploadJobResponse(jobID=jobID, success=True)

    def RegisterWorker(self, request: A.RegisterWorkerRequest, context: grpc.ServicerContext) -> A.RegisterWorkerResponse:
        print(f"RegisterWorker called with: {request}")
        return A.RegisterWorkerResponse(success=True)

    def ReportTaskCompletion(self, request: A.ReportTaskRequest, context: grpc.ServicerContext) -> A.ReportTaskResponse:
        # 更新任务状态
        job: Job = JOB_DICT[request.jobID]
        with job.lock:
            pass

        print(f"ReportTaskCompletion called with: {request}")
        return A.ReportTaskResponse(success=True)


Master_IP = "localhost"
Master_Port = 50051


def serve() -> None:
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=100))
    B.add_MasterServicer_to_server(MasterServicer(), server)
    serverAddress = f"{Master_IP}:{Master_Port}"
    server.add_insecure_port(serverAddress)
    server.start()
    server.wait_for_termination()


def run_server_in_background():
    server_thread = threading.Thread(target=serve, daemon=True)
    server_thread.start()
    print("Server is running in the background...")


if __name__ == '__main__':
    run_server_in_background()
    # 在这里，您可以添加其他的逻辑或者无限循环，以保持主线程活跃。
    # 例如：
    while True:
        # 这里可以执行其他任务
        print("滴答")
        time.sleep(20)
        pass


class ExpiringDict:
    def __init__(self):
        self.store = {}  # 存储数据的字典
        self.timers = {}  # 存储计时器的字典

    def set(self, key, value):
        if key in self.store:
            self.reset_timer(key)  # 如果键已存在，重置计时器
        else:
            self.store[key] = value  # 存储新数据
            self.start_timer(key)    # 启动新的计时器

    def start_timer(self, key):
        timer = threading.Timer(60.0, self._remove, args=(key,))
        timer.start()
        self.timers[key] = timer  # 存储计时器

    def reset_timer(self, key):
        if key in self.timers:
            self.timers[key].cancel()  # 取消当前计时器
            del self.timers[key]         # 从存储中删除计时器
        self.start_timer(key)          # 重新启动计时器

    def _remove(self, key):
        if key in self.store:
            del self.store[key]
            print(f"键 '{key}' 的值已在60秒后被删除。")
        if key in self.timers:
            del self.timers[key]  # 从计时器字典中删除

    def get(self, key):
        value = self.store.get(key, None)
        if value is not None:
            self.reset_timer(key)  # 如果存在，则重置计时器
        return value

    def __repr__(self):
        return repr(self.store)


# 示例
expiring_dict = ExpiringDict()

# 添加一些值到字典
expiring_dict.set("key1", "value1")
print("当前字典：", expiring_dict)

# 等待10秒，访问 key1
time.sleep(10)
print("访问 'key1'：", expiring_dict.get("key1"))  # 访问，重置计时器
print("访问后字典：", expiring_dict)

# 等待60秒，key1不应该被删除
time.sleep(60)
print("60秒后字典：", expiring_dict)

# 再次访问 key1，重置计时器
print("再次访问 'key1'：", expiring_dict.get("key1"))
print("再次访问后字典：", expiring_dict)

# 再次等待60秒后，key1应该仍然存在
time.sleep(60)
print("120秒后字典：", expiring_dict)

# 添加另一个值
expiring_dict.set("key2", "value2")
print("添加key2后字典：", expiring_dict)

# 等待70秒，以确认key2被删除
time.sleep(70)
print("70秒后字典：", expiring_dict)

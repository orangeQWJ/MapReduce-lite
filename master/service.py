from concurrent import futures
from enum import Enum
import queue
import threading
import time
from typing import Dict, List, Optional, Tuple
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
    WAITING = "waiting"  # 等待被分配
    ASSIGNED = "assigned"  # 已经被分配
    FINISH = "finished"  # 顺利结束
    FAILED = "failed"  # 执行失败
    NEED_RESATRT = "need_restart"  # "需要被重启"
    DONE = "done"  # 总Job完成


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
    def __init__(self, job_id: str, task_type: taskType, task_index: int):
        self.job_id: str = job_id
        self.task_id: int = task_index
        self.task_type: taskType = task_type
        self.function_path: filePath = JOB_DICT[job_id].map_reduce_func_path
        if task_type == taskType.MAP:
            self.file_path: List[filePath] = [
                JOB_DICT[job_id].file_for_map[task_index]]
        else:
            for x in JOB_DICT[job_id].file_for_reduce:
                assert len(
                    x) == JOB_DICT[job_id].reduce_num, "reduce 任务所需要的中间文件不存在"
            self.file_path: List[filePath] = [x[task_index]
                                              for x in JOB_DICT[job_id].file_for_reduce]


class taskProgress():
    def __init__(self, job_id: str, task_type: taskType, task_index: int, interval: int = 10):
        self.job_id: str = job_id
        self.task_type: taskType = task_type
        self.task_index: int = task_index
        self.task_status: taskStatus = taskStatus.WAITING
        self.task_status_lock: threading.Lock = threading.Lock()
        self.task_allocation_time: None | int = None
        self.worker: serverAddress | None = None
        self.query_alive_interval: int = interval

    def cancel(self) -> None:
        self.task_status = taskStatus.WAITING
        self.task_allocation_time = None
        self.worker = None

    def assign(self) -> Tuple[bool, Optional[serverAddress | None]]:
        # FIXME:
        return True, None

    """
    def put_task_to_queue(self) -> None:
        task = Task(
            job_id=self.job_id,
            task_type=self.task_type,
            task_index=self.task_index,
        )
        taskQueue.put(task)
    """

    def check_worker_alive(self) -> bool:
        assert self.worker != None, "没有分配work,但是在做心跳检查"
        if worker_heartbeat_dict.get(self.worker.identity()) == None:
            return False
        return True

    """
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
                    self.put_task_to_queue()
                time.sleep(self.query_alive_interval)
    """

    def monitor(self) -> None:
        while True:
            time.sleep(1)  # 其他threading有机会获取lock
            # reduce 任务要等到JOB进行到REDUCE阶段才能运行
            if self.task_type == taskType.REDUCE and JOB_DICT[self.job_id].status == jobStatus.MAPPING:
                # NOTE: job.status == REDUCING, redcue task执行中可能需要重启map taks.
                # NOTE: job.status == MAPPING, 不可能需要 reduce task
                assert self.task_status == taskStatus.WAITING
                pass
            with self.task_status_lock:
                if self.task_status == taskStatus.WAITING:
                    # NOTE: assign 可能会阻塞
                    success, worker = self.assign()
                    if success:
                        assert worker != None
                        self.worker = worker
                        self.task_status = taskStatus.ASSIGNED
                    else:
                        self.task_status = taskStatus.WAITING
                elif self.task_status == taskStatus.ASSIGNED:
                    assert self.worker != None, "DOING 状态一定分配了worker"
                    if self.check_worker_alive():
                        time.sleep(self.query_alive_interval)
                    else:
                        self.task_status = taskStatus.WAITING
                elif self.task_status == taskStatus.FINISH:
                    continue
                elif self.task_status == taskStatus.NEED_RESATRT:
                    self.task_status = taskStatus.WAITING
                elif self.task_status == taskStatus.DONE:
                    return

    def monitor_in_background(self) -> None:
        monitor_thread = threading.Thread(target=self.monitor)
        monitor_thread.start()


class Job:
    def __init__(self, request: A.UploadJobRequest, job_id: str):
        self.lock: threading.Lock = threading.Lock()  # 添加锁以避免竞争条件
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
                                task_index=i)
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

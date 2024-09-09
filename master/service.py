from concurrent import futures
from enum import Enum
import queue
import threading
import time
from typing import Dict, List, Optional, Union
import uuid

import grpc

from gen import service_pb2 as A
from gen import service_pb2_grpc as B


# 任务执行的阶段


class jobStatus(Enum):
    WAITING = "waiting"
    MAPPING = "mapping"
    REDUCING = "reducing"
    FINISH = "finished"


class taskStatus(Enum):
    WAITING = "waiting"
    DOING = "doing"
    FINISH = "finished"


class taskType(Enum):
    MAP = "map"
    REDUCE = "reduce"


class serverAddress:
    def __init__(self, ip: str, port: int):
        self.ip: str = ip
        self.port: int = port


class filePath:
    def __init__(self, server: serverAddress, path: str):
        self.serverAddress: serverAddress = server
        self.path: str = path


class Job:
    def __init__(self, request: A.UploadJobRequest, job_id: str):
        self.lock = threading.Lock()  # 添加锁以避免竞争条件
        self.job_id: str = job_id
        self.map_num: int = request.mapNum
        self.reduce_num: int = request.reduceNum
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
        self.file_for_reduce: List[List[Optional[filePath]]] = [
            [None for _ in range(request.reduceNum)]
            for _ in range(request.mapNum)
        ]
        self.status: jobStatus = jobStatus.WAITING
        self.map_task_status: List[taskStatus] = [
            taskStatus.WAITING for _ in range(request.mapNum)]
        self.reduce_task_status: List[taskStatus] = [
            taskStatus.WAITING for _ in range(request.reduceNum)]

    def some_method(self):  # 示例方法，示范如何使用锁
        with self.lock:
            # 进行线程安全操作
            pass


class Task:
    def __init__(self, job_id: str, task_type: taskType, task_id: int, file_path: List[filePath]):
        self.job_id: str = job_id
        self.task_id: int = task_id
        self.task_type: taskType = task_type
        self.file_path: List[filePath] = file_path

        # 记录正在执行的任务
JOB_DICT: Dict[str, Job] = dict()

# job队列
jobQueue = queue.Queue()
# task队列,由job拆分得到
taskQueue = queue.Queue()
# 空闲worker队列
workerQueue = queue.Queue()


def generate_map_task():
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
                                task_id=i, file_path=[job.file_for_map[i]])
                taskQueue.put(map_task)
                job.map_task_status[i] = taskStatus.DOING
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

from enum import Enum
from concurrent import futures
import grpc
import threading
import time
import uuid

from gen.service_pb2 import *
from gen import service_pb2_grpc as B

JOBDICT = {}


class JobStatus(Enum):
    WAITING = "waiting"
    MAPPING = "mapping"
    REDUCING = "reducing"
    FINISH = "finished"

import queue

jobQueue = queue.Queue()
taskQueue = queue.Queue()




class MasterServicer(B.MasterServicer):
    def UploadJob(self, request: UploadJobRequest, context: grpc.ServicerContext) -> UploadJobResponse:
        for path in request.filePaths:
            print(path.path)
        jobID = str(uuid.uuid4())
        job ={
            "mapNum": request.mapNum,
            "reduceNum": request.reduceNum,
            "clientServerAddress": {
                "ip": request.serverAddress.ip,
                "port": request.serverAddress.port
            },
            "mapReduceFuncPath": {"ip": request.mapReduceFuncPath.serverAddress.ip,
                                  "port": request.mapReduceFuncPath.serverAddress.port,
                                  "path": request.mapReduceFuncPath.path
                                  },
            "mapfilePaths": [{"ip": path.serverAddress.ip,
                              "port": path.serverAddress.port,
                              "path": path.path} for path in request.filePaths],
            "middleFilePaths": [[None for _ in range(request.reduceNum)] for _ in range(request.mapNum)],
            "status": JobStatus.WAITING,

        }
        JOBDICT[jobID] = job
        jobQueue.put(job)
        return UploadJobResponse(jobID=jobID, success=True)

    def RegisterWorker(self, request: RegisterWorkerRequest, context: grpc.ServicerContext) -> RegisterWorkerResponse:
        print(f"RegisterWorker called with: {request}")
        return RegisterWorkerResponse(success=True)

    def ReportTaskCompletion(self, request: ReportTaskRequest, context: grpc.ServicerContext) -> ReportTaskResponse:
        print(f"ReportTaskCompletion called with: {request}")
        return ReportTaskResponse(success=True)


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

jobDict = {
    "jobID": "exampleJobID",
    "mapNum": 2,
    "reduceNum": 2,
    "userserverAddress": {
        "ip": "IP_ADDRESS",
        "port": 50051
    },
    "mapReduceFuncPath": {
        "path": "examplePath"
    },


}

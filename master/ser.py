from concurrent import futures
import grpc
import threading
import time

from gen.service_pb2 import *
from gen import service_pb2_grpc as A


class MasterServicer(A.MasterServicer):
    def UploadJob(self, request: UploadJobRequest, context: grpc.ServicerContext) -> UploadJobResponse:
        # print(f"UploadTask called with: {request}")
        #print(f"request: {request}")
        for path in request.filePaths:
            print(path.path)
        return UploadJobResponse(jobID="exampleJobID", success=True)

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
    A.add_MasterServicer_to_server(MasterServicer(), server)
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


from concurrent import futures
import grpc
from typing import Tuple

from gen.master import master_pb2_grpc, master_pb2
 

class MasterService(master_pb2_grpc.MasterServiceServicer):

    def UploadTask(self, request: master_pb2.UploadTaskRequest, context: grpc.ServicerContext) -> master_pb2.UploadTaskResponse:
        print("UploadTask called with:")
        print(f"mNum: {request.mNum}, rNum: {request.rNum}, serverAddress: {request.serverAddress.ip}:{request.serverAddress.port}")
        print(f"mapReduceFuncPath: {request.mapReduceFuncPath.path}")
        for fp in request.filePaths:
            print(f"FilePath: {fp.path}")
        return master_pb2.UploadTaskResponse(jobID="1234", success=True)

    def RegisterWorker(self, request: master_pb2.RegisterWorkerRequest, context: grpc.ServicerContext) -> master_pb2.RegisterWorkerResponse:
        print("RegisterWorker called with:")
        print(f"ServerAddress: {request.server_add.ip}:{request.server_add.port}")
        return master_pb2.RegisterWorkerResponse(success=True)

    def ReportTaskCompletion(self, request: master_pb2.ReportTaskRequest, context: grpc.ServicerContext) -> master_pb2.ReportTaskResponse:
        print("ReportTaskCompletion called with:")
        print(f"jobID: {request.jobID}, taskType: {request.taskType}, taskID: {request.taskID}")
        for fp in request.filePaths:
            print(f"FilePath: {fp.path}")
        return master_pb2.ReportTaskResponse(success=True)

def serve() -> None:
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    master_pb2_grpc.add_MasterServiceServicer_to_server(MasterService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        server.wait_for_termination()
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()




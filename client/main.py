from concurrent import futures
import grpc
import threading

from gen.service_pb2 import *
from gen import service_pb2_grpc as A

from typing import Iterator

from util import *


class ClientServiver(A.ClientServicer):
    def ReadFile(self, request: ReadFileRequest, context: grpc.ServicerContext) -> Iterator[FileChunk]:
        file_content = b"Hello, world!"
        yield FileChunk(content=file_content)
        filePath = request.filePath
        with open(filePath, 'rb') as file:
            while True:
                piece = file.read(1024)
                if not piece:
                    break
                yield FileChunk(content=piece)

    def ReportCompletion(self, request: ReportCompletionRequest, context: grpc.ServicerContext) -> ReportCompletionResponse:
        print(f"ReportCompletion request received: {request.jobID}")
        for path in request.filePaths:
            print(
                f"serverAddress: {path.serverAddress.ip}:{path.serverAddress.port}, path: {path.path}")
            # TODO: 通过rpc 拉取这些文件
        return ReportCompletionResponse(success=True)


Client_IP = get_lan_ip()
Client_Port = 0


def serve() -> None:
    global Client_Port
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    A.add_ClientServicer_to_server(ClientServiver(), server)
    Client_Port = server.add_insecure_port(f"{Client_IP}:{0}")
    server.start()
    server.wait_for_termination()


def run_server_in_background() -> None:
    server_thread = threading.Thread(target=serve, daemon=True)
    server_thread.start()
    print(f"Server started on {Client_IP}:{Client_Port}")


MasterIP = "localhost"
MasterPort = 50051


def uploadjob(M: int, N: int, mapReduceFuncPath: str, hugeFilePath: str):
    master_server_add = f"{MasterIP}:{MasterPort}"
    splited_file_paths = simple_split_file(hugeFilePath, M)
    channel = grpc.insecure_channel(master_server_add)
    stub = A.MasterStub(channel)

    filePaths = [FilePath(serverAddress=ServerAddress(
        ip="ClientIP", port=50051), path=x) for x in splited_file_paths]

    request = UploadJobRequest(
        mapNum=M,
        reduceNum=N,
        serverAddress=ServerAddress(ip="ClientIP", port=888888),
        mapReduceFuncPath=FilePath(serverAddress=ServerAddress(
            ip="ClientIP", port=50051), path=mapReduceFuncPath),
        filePaths=filePaths
    )

    # 调用服务
    response = stub.UploadJob(request)
    # 打印响应
    print("UploadTask response:", response)
    channel.close()


uploadjob(4, 3, "mapReduceFuncPath",
          "/Users/bytedance/code/MapReduce-lite/test/hugefile.txt")

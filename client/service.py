import time
from concurrent import futures
import threading
from typing import Iterator

import grpc

from gen import service_pb2_grpc as A
from gen.service_pb2 import *
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


CLIENT_IP = get_lan_ip()
CLIENT_PORT = 0


def serve() -> None:
    global CLIENT_PORT
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    A.add_ClientServicer_to_server(ClientServiver(), server)
    CLIENT_PORT = server.add_insecure_port(f"{CLIENT_IP}:{0}")
    server.start()
    server.wait_for_termination()


def run_server_in_background() -> None:
    server_thread = threading.Thread(target=serve, daemon=True)
    server_thread.start()
    time.sleep(1)  # print 的执行可能会早于CLIENT_PORT 的更新
    print(f"Server started on {CLIENT_IP}:{CLIENT_PORT}")


if __name__ == '__main__':
    run_server_in_background()
    while True:
        print("滴答")
        time.sleep(3)
        pass

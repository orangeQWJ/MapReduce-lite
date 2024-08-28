import grpc
from gen.master.master_pb2 import UploadTaskRequest
from gen.master.master_pb2_grpc import MasterServiceStub
from gen.common.common_pb2 import FilePath, ServerAddress


masterIP = "localhost"
masterPort = 50051

def upload_task(m_num :int, r_num: int, funcPath: str, file_paths):
    masterServerAddress = f"{masterIP}:{masterPort} "
    channel = grpc.insecure_channel(masterServerAddress)
    stub = MasterServiceStub(channel)

    filePathList = [FilePath(ServerAddress(ip="Client_IP_ADDRESS", port=7789797), path=fp) for fp in file_paths]
    funcPath1 = FilePath(ServerAddress(ip="Client_IP_ADDRESS", port=7789797), path=funcPath)

    request = UploadTaskRequest(
        mNum=m_num,
        rNum=r_num,
        serverAddress=ServerAddress(ip="IP_ADDRESS", port=50052), 
        mapReduceFuncPath=funcPath1,
        filePaths= filePathList
    )
    response = stub.UploadTask(request)

    channel.close()
    return response

upload_task(m_num=2, r_num=3, funcPath="mapReducePath", file_paths=["filePath1", "twofilePath"])

import socket

def get_local_ip():
    # 创建一个socket对象
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 不需要真的连接，只是为了获取IP地址
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip



if __name__ == "__main__":
    # 填写服务器地址
    server_address = "localhost:50051"


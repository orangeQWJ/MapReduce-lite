import grpc

from gen.service_pb2 import *
from gen import service_pb2_grpc as A


from util import *

from config import MASTER_IP, MASTER_PORT


CLIENT_IP = get_lan_ip()
CLIENT_PORT = 0

JOB_ID = ""


def upload_job(M: int, N: int, map_reduce_func_path: str, huge_file_path: str):
    master_server_add = f"{MASTER_IP}:{MASTER_PORT}"
    channel = grpc.insecure_channel(master_server_add)
    stub = A.MasterStub(channel)

    splited_file_paths = simple_split_file(huge_file_path, M)

    client_server_add = ServerAddress(ip=CLIENT_IP, port=CLIENT_PORT)

    file_path_list = [FilePath(serverAddress=client_server_add, path=x)
                      for x in splited_file_paths]

    request = UploadJobRequest(
        mapNum=M,
        reduceNum=N,
        serverAddress=client_server_add,
        mapReduceFuncPath=FilePath(
            client_server_add, path=map_reduce_func_path),
        filePaths=file_path_list
    )

    # 调用服务
    global JOB_ID
    response: UploadJobResponse = stub.UploadJob(request)
    JOB_ID = response.jobID

    # 打印响应
    # TODO: 处理response
    print("UploadTask response:", response)
    channel.close()


upload_job(4, 3, "mapReduceFuncPath",
           "/Users/bytedance/code/MapReduce-lite/test/hugefile.txt")

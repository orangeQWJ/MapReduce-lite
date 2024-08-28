from concurrent import futures
import grpc

import sys
sys.path.append(".")
import gen.master.master_pb2 as A
import gen.master.master_pb2_grpc as B
 
class MasterService(B.MasterServiceServicer):
    def UploadTask(self, request, context): 
        print(request)



def serve() -> None:
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    B.add_MasterServiceServicer_to_server(MasterService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        server.wait_for_termination()
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()




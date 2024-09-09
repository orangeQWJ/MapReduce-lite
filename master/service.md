```python
class Job:
    def __init__(self, request, JobStatus):
        self.mapNum = request.mapNum
        self.reduceNum = request.reduceNum
        self.clientServerAddress = {
            "ip": request.serverAddress.ip,
            "port": request.serverAddress.port
        }
        self.mapReduceFuncPath = {
            "ip": request.mapReduceFuncPath.serverAddress.ip,
            "port": request.mapReduceFuncPath.serverAddress.port,
            "path": request.mapReduceFuncPath.path
        }
        self.mapfilePaths = [
            {
                "ip": path.serverAddress.ip,
                "port": path.serverAddress.port,
                "path": path.path
            } for path in request.filePaths
        ]
        # M task产生的中间文件, M * N
        self.middleFilePaths = [
            [None for _ in range(request.reduceNum)] for _ in range(request.mapNum)
        ]
        self.status = JobStatus.WAITING

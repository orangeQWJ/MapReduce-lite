import os
import hashlib
import json


class MapReduceEmitter:
    def __init__(self, n, output_dir=None):
        """
        初始化 MapReduceEmitter。

        参数:
        n: 分区数，将键值对分到 n 个文件中。
        output_dir: 输出目录，存放所有文件的目录。若未指定，则使用当前运行目录。
        """
        self.n = n
        # 若未指定 output_dir，则使用当前运行目录
        if output_dir is None:
            output_dir = os.getcwd()

        self.output_dir = output_dir

        # 确保输出目录存在
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # 创建文件对象列表
        self.files = [
            open(os.path.join(output_dir, f"output_{i}.json"), 'a') for i in range(n)]

    def emit(self, key, value):
        """
        将 (key, value) 键值对以 JSON 格式写入到合适的文件中。

        参数:
        key: 键，用于确定写入到哪个文件。
        value: 值，将与键一起写入文件。
        """
        # 计算键的 hash 值，确定文件编号
        file_index = self._get_file_index(key)

        # JSON 编码键值对
        json_data = json.dumps({"key": key, "value": value})

        # 将 JSON 数据写入到指定的文件
        self.files[file_index].write(json_data + "\n")

    def _get_file_index(self, key):
        """
        根据键计算 hash 值并返回文件索引。

        参数:
        key: 用于计算索引的键。

        返回:
        对应的文件索引，范围从 0 到 n-1。
        """
        # 使用 MD5 哈希来确保一致性
        hash_value = int(hashlib.md5(str(key).encode('utf-8')).hexdigest(), 16)
        return hash_value % self.n

    def close_files(self):
        """
        关闭所有文件。
        """
        for f in self.files:
            f.close()


# 示例调用
emitter = MapReduceEmitter(n=4)  # 分成 4 个文件
data = [("key1", "value1"), ("key2", "value2"),
        ("key3", "value3"), ("key4", "value4")]

# 将数据通过 emit 函数写入到不同的文件中
for key, value in data:
    emitter.emit(key, value)

# 关闭所有文件
emitter.close_files()


import os
import json
from concurrent.futures import ThreadPoolExecutor

def sort_file_by_key(file_path):
    """
    读取指定文件中的每一行数据，按照 key 进行排序，并将排序后的数据写回到原文件中。

    参数:
    file_path: 文件路径，需要排序的文件的路径。
    """
    data_list = []
    with open(file_path, 'r') as file:
        for line in file:
            data = json.loads(line.strip())  # 解析 JSON 数据
            data_list.append(data)
    
    # 按照 'key' 进行排序
    data_list.sort(key=lambda x: x['key'])

    # 将排序后的数据写回到原文件
    with open(file_path, 'w') as file:
        for data in data_list:
            file.write(json.dumps(data) + "\n")

    print(f"File sorted and written back to {file_path}")

def sort_files_in_directory(directory, prefix, suffix, max_workers=8):
    """
    遍历指定目录下所有以 prefix 开头，suffix 结尾的文件，使用多线程并发调用排序函数进行排序。

    参数:
    directory: 文件夹路径，存放需要排序的文件。
    prefix: 文件前缀，用于筛选文件。
    suffix: 文件后缀，用于筛选文件。
    max_workers: 最大线程数，用于控制并发的线程数量。
    """
    # 需要排序的文件列表
    files_to_sort = [
        os.path.join(directory, file_name)
        for file_name in os.listdir(directory)
        if file_name.startswith(prefix) and file_name.endswith(suffix)
    ]

    # 使用线程池并发处理文件排序
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        executor.map(sort_file_by_key, files_to_sort)

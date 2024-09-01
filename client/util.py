import os
import socket

def simple_split_file(file_path, m):
    if m <= 0:
        raise ValueError("The number of parts must be greater than 0")
    
    # 准备分割文件的路径
    base_name, extension = os.path.splitext(os.path.basename(file_path))
    dir_name = os.path.dirname(file_path)
    new_files_paths = []
    new_files = []

    # 创建新文件并打开以待写入
    for i in range(m):
        new_file_name = f"{base_name}_part{i+1}{extension}"
        new_file_path = os.path.join(dir_name, new_file_name)
        new_files_paths.append(os.path.abspath(new_file_path))
        new_files.append(open(new_file_path, 'w', encoding='utf-8'))

    # 轮流向每个文件写入行
    with open(file_path, 'r', encoding='utf-8') as file:
        for i, line in enumerate(file):
            # 确定当前行应该写入哪个文件
            file_index = i % m
            new_files[file_index].write(line)
    
    # 关闭所有新文件
    for new_file in new_files:
        new_file.close()

    return new_files_paths


def get_lan_ip():
    # 创建一个socket对象
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # 尝试连接到一个不存在的地址，目的是获取当前活动的网络接口的IP地址
        s.connect(("10.255.255.255", 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = "127.0.0.1"
    finally:
        s.close()
    return IP

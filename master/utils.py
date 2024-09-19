import threading
import time


# 一个带有生命周期的键值存储
class ExpiringDict:
    def __init__(self, deadline_seconds=60):
        self.store = {}  # 存储数据的字典
        self.timers = {}  # 存储计时器的字典
        self.deadline_seconds = deadline_seconds  # 过期时间（秒）

    def set(self, key: str, value: int, duration: int = 60):
        # 存储新数据
        self.store[key] = value

        # 如果当前有计时器，则取消并删除
        if key in self.timers:
            self.timers[key].cancel()

        # 启动新的计时器
        timer = threading.Timer(duration,
                                self._remove, args=(key,))
        # timer.daemon=True
        timer.start()
        self.timers[key] = timer  # 存储计时器

    def _remove(self, key: str):
        if key in self.store:
            del self.store[key]
            # TODO: Log
            print(f"键 '{key}' 已删除。")
        if key in self.timers:
            del self.timers[key]  # 从计时器字典中删除

    def get(self, key: str):
        # 直接返回存储的值
        return self.store.get(key, None)

    def __repr__(self):
        return repr(self.store)


if __name__ == "__main__":
    # 示例
    expiring_dict = ExpiringDict()

    # 添加一些值到字典
    expiring_dict.set("key1", 1, 10)
    expiring_dict.set("key2", 2, 10)
    expiring_dict.set("key3", 3, 10)

    print("当前字典：", expiring_dict)

    time.sleep(8)
    expiring_dict.set("key1", 1)
    print("set key1")

    time.sleep(3)
    # 等待60秒，key1应该被删除
    print("11秒后字典：", expiring_dict)

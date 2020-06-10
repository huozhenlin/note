"""
lru 算法
最近最少使用算法
基本思路：利用linkedhashmap，存放数据，若数据在linkedhashmap中不存在，则在数据库取出写入到
表头；若在linkedhashmap中存在，则取出并且移动数据至表头。若不存在且linedhashmap容量已慢
则删除linkedhashmap最后的键值对删除，从数据库取出数据放至表头
"""

from collections import OrderedDict
class LRUCacheDemo():
    queue2 = {"0001":{"name":"小马"}, "00002":{"name":"小猪"}} #模拟数据库数据
    def __init__(self):
        self.queue = OrderedDict({"0004":{"name":"小红"}, "00007":{"name":"小白"}})
        self.maxSize = 3


    def put(self, key, data):
        if len(self.queue.keys()) >= self.maxSize:
            print("缓存已满，准备删除最后的数据")
            old_key, old_value = self.queue.popitem(last=False)
            if old_key:
                print("{}已经删除".format(old_key))

        print("准备写入新数据")
        self.queue[key] = data
        print("写入新数据完成")

    def get(self, key):
        if key not in self.queue:
            data = LRUCacheDemo.queue2.get(key)
            self.put(key, data)
        data = self.queue.pop(key)
        print("=====")
        print(data)
        print("======")
        print("获取到数据{}".format(data))
        print("移动数据至表头")
        self.queue[key] = data

        print(self.queue)


lrudemo = LRUCacheDemo()
lrudemo.get("00002")
lrudemo.get("0001")
lrudemo.get("00002")

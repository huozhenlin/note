#!/usr/bin/env python
# _*_ encoding:utf-8 _*_

import socket
import select


class Reqest:
    def __init__(self, sk, info):
        self.sk = sk
        self.info = info

    def fileno(self):
        return self.sk.fileno()


class AsyncMod:
    def __init__(self):
        self.sk_list = []
        self.conns = []

    def add_request(self, req_info):
        """
        创建请求
        :return:
        """
        sk = socket.socket()
        sk.setblocking(False)
        try:
            sk.connect((req_info["host"], req_info["port"]))   # 连接的请求已经发出去了
        except BlockingIOError as e:
            pass
        obj = Reqest(sk, req_info)
        self.sk_list.append(obj)
        self.conns.append(obj)

    def run(self):
        """
        开始事件循环,检测连接是否成功，数据是否返回？
        :return:
        """
        while True:
            # select.select([socket对象])
            # 不一定是socket对象，可是任何任何对象，对象一定要有fileno方法
            r, w, e = select.select(self.sk_list, self.conns, [], 0.05)
            # 是否连接成功
            for obj in w:
                # 检查obj是哪个字典
                data = "GET %s http/1.1\r\nhost:%s\r\n\r\n" % (obj.info["path"], obj.info["host"])
                # print(data)
                obj.sk.send(data.encode("utf-8"))
                self.conns.remove(obj)
            # 数据返回，接收到数据
            for obj in r:
                response = obj.sk.recv(8096)
                print(obj.info["host"], response)
                obj.info["callback"](response)
                self.sk_list.remove(obj)
            # 所有的请求已经返回
            if not self.sk_list:
                break


def done(response):
    print(response)


url_list = [
    {"host": "www.baidu.com", "port": 80, "path": "/", "callback": done},
    {"host": "www.cnblogs.com", "port": 80, "path": "/", "callback": done},
    {"host": "www.bing.com", "port": 80, "path": "/", "callback": done},
]

am = AsyncMod()
for item in url_list:
    am.add_request(item)

am.run()
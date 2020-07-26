# 前言  
使用redis队列存放消息时，我们通常用rpop,lpop,或者brpop取出队列中存放的数据。  


# 同步阻塞模型
同步阻塞模型也就是，代码从上到下按顺序执行，遇到函数调用，则调用函数，阻塞等待结果返回，然后
继续循环调用。  

该方法有哪些缺点呢？
1. 对cpu的利用率低下，也就是消费速度低于生成速度，容易造成队列堵塞，从而造成
消息丢失等一系列问题。

python实现代码如下  
```python
from redis import Redis
import time

def analyse(data):
    """
    数据分析器
    """
    time.sleep(2) #模拟解析数据所需时间
    return data
    
    
def run():
    cli = Redis(host='127.0.0.1', db=0)
    while True:
        # 方法一
        # 同步阻塞程序
        item = cli.brpop('test', 0)
        result = analyse(bytes.decode(item[1]))
       
```

# 同步非阻塞模型  
为了解决第一种模型带来的性能低下问题，我们可以实例化多个消费者，并发去消费信息，或者通过多线程，
实现主线程取消息，子线程消费消息。这也是目前最容易被接纳的方案。  

该方法有哪些优缺点呢？
优点：
1. 充分利用cpu的性能，在java等其他语言上，甚至能利用多核cpu的优势，在同一时间同时并发执行，但在
python上，由于全文解析器锁（GIL）锁对象的存在，cpu每刻只能保持一个线程在运行。
缺点：  
1. 线程切换也是需要时间的
2. 每个线程都占用内存    

因此，对于内存占用不太关心的服务，可以采用这种方案。 

```python
from concurrent.futures import ThreadPoolExecutor
import time
from redis import Redis
cli = Redis(host='127.0.0.1', db=0)

def callback(future):
    # 模拟持久化到数据库
    time.sleep(1)
    print(future.result())

def analyse(data):
    """
    数据分析器
    """
    time.sleep(2) #模拟解析数据所需时间
    return data

def run():
    pool = ThreadPoolExecutor(max_workers=4) #线程池，最多四个线程
    while True:
        # 方法二
        try:
            # 多线程处理
            # 当前肯定是个阻塞操作，不过没关系，主线程负责取数据，子线程负责解析数据，添加回调完成写入数据库
            item = cli.brpop('test', 0)
            future = pool.submit(analyse, bytes.decode(item[1]))
            future.add_done_callback(callback)
        except:
            pool.shutdown(wait=True)
```

# 异步非阻塞模型  
上面介绍的第二种办法，已经可以让消费速度跟上生产速度了。为了将cpu的性能压缩到极致，同时，节省内存，下面，我们可以尝试去
编写一个异步非阻塞的模型，实现对消息的消费。 

开始之前，我们先了解下异步io
所谓异步io，即是进行io操作的时候，不会等待结果方法，继续执行其他的事情，结果返回了，可以通过回调提醒应用程序处理。    

在操作系统上，实现异步io，有以下三大底层模块可供选择  
1. select  文件描述符fd，存放在数组中，最大可存储1024个文件描述符，通过循环遍历的方式，取出就绪的可读或者可写的消息
2. poll  文件描述符fd，存放在链表中，没有存储限制，和select一样，通过循环遍历的方式，取出就绪的可读或者可写的消息
3. epoll  文件描述符fd，存放在链表中，没有存储限制，通过回调的方法，取出可读或者可写的消息，相比于select和poll，性能最高

我们看下实例，使用select和socket，编写一个简单的异步非阻塞的通信程序  


server端程序
```python
import socket
import select

sk1 = socket.socket()
sk1.bind(('0.0.0.0', 8001))
sk1.listen()

sk2 = socket.socket()
sk2.bind((('0.0.0.0', 8002)))
sk2.listen()

sk3 = socket.socket()
sk3.bind(('0.0.0.0', 8003))
sk3.listen()

inputs  =[sk1, sk2, sk3]

while True:
    r_list, w_list, e_list = select.select(inputs, [], inputs, 1)
    for sk in r_list:
        print(sk)
        conn, address = sk.accept()
        conn.sendall(bytes('hello', encoding='utf-8'))
        conn.close()

    for sk in e_list:
        inputs.remove(sk)

```

client端程序  
```python
import socket


obj = socket.socket()
obj.connect(('127.0.0.1', 8081))

while True:
    inp = input('>>>')
    print(inp)
    obj.sendall(bytes(inp, encoding='utf-8'))
    ret = str(obj.recv(1024),encoding='utf-8')
    print(ret)

obj.close()
```

回到我们的redis，要先实现同一线程中，我们一边取出消息，另一边，在解析信息的信息，不会发生堵塞。我们需要了解到
协程知识   
所谓协程，也就是他能记住代码上一次的运行位置，在进行io操作的时候，可以不必等待，跳到另一个方法执行，当结果
返回时，可以跳回到当前方法，得到结果继续往下运行  

```python
import asyncio
from redis import Redis
cli = Redis(host='127.0.0.1', db=0)

async def analyse(data):
    #time.sleep(2)
    await asyncio.sleep(2) # 模拟解析所需时间
    return data

# 方法三
# 只开一个线程完成异步操作，效果相当于多线程的同步操作

async def task():
    loop = asyncio._get_running_loop()
    while True:
        fut = loop.create_future() #创建future任务
        item = cli.brpop('test', 0)
        loop.create_task(set_after(fut, bytes.decode(item[1]))) #通过yield返回
        #fut = loop.run_in_executor(None, analyse,bytes.decode(item[1]) ) # 底层实际是通过多线程处理
        yield fut

async def set_after(future, data):
    result = await analyse(data)
    future.set_result(result)


async def main():
    tasks = []
    async for data in task():
        tasks.append(data)
        if len(tasks) >= 5: #通过设置5个任务，同时执行，本来一个任务执行需要2秒，5个任务同时执行，理论上也需要2秒
            result = await asyncio.gather(*tasks)
            print(result)
            tasks.clear()
        # print(data.result())


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
```





























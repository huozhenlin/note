import time, asyncio, aiohttp

"""
协程就是线程和进程的升级版，对于io密集性的任务，推荐使用协程处理。
协程的原理就是将任务放进一个任务池，交由cpu处理，其中，每个任务都有自己的状态，
完成时会发出通知，让用户取出
tornado框架底层异步实现是使用了epoll。
select poll epoll三大异步组件的区别  
select:
连接数受限
查找配对速度慢
数据由内核拷贝到用户态
poll改善了第一个缺点
epoll改了三个缺点.
"""


url = 'http://127.0.0.1:8888/hotel/gg'
async def hello(url, semaphore):
    async with semaphore:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, verify_ssl=False, timeout=5) as response:
                status = response.status
                print(status)
                return await response.read()

async def run():
    semaphore = asyncio.Semaphore(500)
    to_get = [hello(url, semaphore) for _ in range(1000)]
    await asyncio.wait(to_get)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
    loop.close()


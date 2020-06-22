
import asyncio
from multiprocessing import Process
from aiohttp import ClientSession

async def print_size(url):
    async with ClientSession() as session:
        async with session.get(url) as response:
            content = await response.read()
            print(response.url)

def start(url):
    asyncio.get_event_loop().run_until_complete(
        print_size(url)
    )


if __name__ == '__main__':
    print("Starting UDP server")

    for i in range(5):
        url = 'http://www.baidu.com?id=%s'%i
        t = Process(target=start, args=(url,))
        t.deamon = True
        t.start()

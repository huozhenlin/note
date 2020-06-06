import time, asyncio, aiohttp

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
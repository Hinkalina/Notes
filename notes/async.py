import asyncio

import aiohttp


async def fetch_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def main():
    urls = [
        'https://www.example.com',
        'https://www.google.com',
        'https://www.python.org',
    ]
    tasks = [asyncio.create_task(fetch_url(url)) for url in urls]
    results = await asyncio.gather(*tasks)
    print(results)


if __name__ == '__main__':
    asyncio.run(main())

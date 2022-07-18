import asyncio

import httpx

from client import get_github_client


async def main():
    async with httpx.AsyncClient() as http_client:
        gh = get_github_client(http_client)


if __name__ == "__main__":
    asyncio.run(main())

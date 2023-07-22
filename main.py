import asyncio

from api import get_posts


async def main():
    posts = await get_posts(page=10, limit=5)
    for post in posts:
        print(post)

if __name__ == "__main__":
    asyncio.run(main())
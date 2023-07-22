import aiohttp
from pydantic import TypeAdapter

from config import API
from models import Post


async def get_posts(page: int, limit: int) -> list[Post]:
    async with aiohttp.ClientSession() as session:
        async with session.get(url=API.format(page=page, limit=limit)) as response:
            adapter = TypeAdapter(list[Post])
            return adapter.validate_python(await response.json())
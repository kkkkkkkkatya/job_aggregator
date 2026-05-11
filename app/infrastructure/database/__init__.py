from contextlib import asynccontextmanager
from typing import AsyncGenerator

from tortoise import Tortoise

from app.common.config import TORTOISE_CONFIG


@asynccontextmanager
async def tortoise_context() -> AsyncGenerator[None, None]:
    await Tortoise.init(config=TORTOISE_CONFIG)
    try:
        yield
    finally:
        await Tortoise.close_connections()

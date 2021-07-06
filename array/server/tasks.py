import asyncio
import os
from typing import Any

from arq import create_pool
from arq.connections import RedisSettings

from services.array import clean_array_avg


REDIS_URL = os.environ.get('REDIS_URL', 'redis://localhost:6379/0')


async def clean_array_avg_task(ctx, array: list[Any]):
    return clean_array_avg(array)


def init_task_pool():
    loop = asyncio.get_event_loop()
    task_pool = loop.run_until_complete(create_pool(RedisSettings.from_dsn(REDIS_URL)))
    return task_pool


pool = init_task_pool()


class WorkerSettings:
    functions = [clean_array_avg_task]
    redis_pool = pool

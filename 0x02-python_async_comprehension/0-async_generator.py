#!/usr/bin/env python3
"""a coroutine called async_generator that takes no arguments"""
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """loops 10 async times, waits for 1sec, yields rand nb 0~10"""

    for i in range(0, 10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

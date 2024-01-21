#!/usr/bin/env python3
"""async basics"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """waits for random secs and returns it"""
    _rand = random.uniform(0, max_delay)
    await asyncio.sleep(_rand)
    return _rand

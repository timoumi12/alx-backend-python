#!/usr/bin/env python3
"""async basics"""
import random
import asyncio


async def wait_random(int max_delay=10):
    """waits for random secs and returns it"""
    rand = random.uniform(0, max_delay)
    await asyncio.sleep(rand)
    return rand

#!/usr/bin/env python3
"""asynchronous coroutine"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """asynchronous coroutine that takes in an integer argument"""
    rand = random.uniform(0, max_delay)
    await asyncio.sleep(rand)
    return rand

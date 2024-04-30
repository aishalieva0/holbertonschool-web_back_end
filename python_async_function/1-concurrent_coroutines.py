#!/usr/bin/env python3
"""asynchronous coroutine"""
from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """return the list of all the delays"""
    all_delays = []
    for _ in range(n):
        all_delays.append(await wait_random(max_delay))
    return sorted(all_delays)

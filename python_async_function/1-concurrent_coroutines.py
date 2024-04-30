#!/usr/bin/env python3
"""asynchronous coroutine"""
wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> float:
    """return the list of all the delays"""
    all_delays = []
    for _ in range(n):
        all_delays.append(await wait_random(max_delay))
    return all_delays

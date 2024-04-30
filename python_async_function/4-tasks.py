#!/usr/bin/env python3
"""contains task_wait_n"""
from typing import List
import asyncio

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """return the list of all the delays"""
    all_delays = []
    for _ in range(n):
        all_delays.append(await task_wait_random(max_delay))
    return sorted(all_delays)

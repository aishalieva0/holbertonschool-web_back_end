#!/usr/bin/env python3
"""Async Generator"""

import random
import asyncio


async def async_generator():
    """yield a random number between 0 and 10"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(1, 10)

#!/usr/bin/env python3
"""Async Generator"""

import random
import asyncio
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None, None]:
    """yield a random number between 0 and 10"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(1, 10)

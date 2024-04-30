#!/usr/bin/env python3
"""Async Comprehensions"""

import random
import asyncio
from typing import Generator

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> Generator[float, None, None]:
    """collect 10 random numbers using an async comprehensing"""
    result = []
    async for i in async_generator():
        result.append(i)
    return result

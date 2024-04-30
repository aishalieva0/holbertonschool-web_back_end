#!/usr/bin/env python3
"""contains task_wait_random"""
from asyncio import Task
import asyncio

wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> Task:
    """r returns a asyncio.Task"""
    task = asyncio.create_task(wait_random(max_delay))
    return task

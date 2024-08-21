#!/usr/bin/env python3
"""
measure_runtime coroutine that will execute
async_comprehension four times in parallel
using asyncio.gathe
"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that measures the total runtime
    of executing async_comprehension
    four times in parallel using asyncio.gather.

    Returns:
        float: The total runtime in seconds.
    """
    start_time = time.time()

    await asyncio.gather(async_comprehension())
    end_time = time.time()
    result = end_time - start_time
    return result

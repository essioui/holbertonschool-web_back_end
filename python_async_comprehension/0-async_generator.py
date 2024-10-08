#!/usr/bin/env python3
"""
async_generator async_generator  takes no argument
Use the random module
"""


import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Coroutine that asynchronously generates 10 random numbers.
    Await:
        delay 1 second

    Yields:
        float: A random number between 0 and 10 after a 1-second delay.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        result = random.uniform(0, 10)
        yield result

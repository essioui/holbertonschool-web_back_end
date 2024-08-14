#!/usr/bin/env python3
"""
this module have function import asyncio and random
"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    function `wait_random` has arg
    max_delay: int with default value = 10
    return: random number float
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

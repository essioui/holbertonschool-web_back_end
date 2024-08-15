#!/usr/bin/env python3
"""
This module defines the task_wait_n function
"""


import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    task_wait_random n times with the specified max_delay
    n: int
    max_delay: int
    returns: float a list of all the delays
    """
    tasks = []
    for _ in range(n):
        task = task_wait_random(max_delay)
        tasks.append(task)

    delays = await asyncio.gather(*tasks)
    return sorted(delays)

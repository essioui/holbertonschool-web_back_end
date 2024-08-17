#!/usr/bin/env python3
"""
this module import 'wait_random' from other file for display list of time wait
"""


from typing import List
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    function return list 
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delay_list = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        delay_list.append(task)
    return delay_list

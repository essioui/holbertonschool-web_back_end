#!/usr/bin/env python3
"""
this module import 'wait_random' from other file for display list of time wait
"""


import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    function return all delays in list and wait when end
    n: int
    max_delay: int
    return: list of type float 
    """
    # create list by use asyncio.create_task
    delays = [asyncio.create_task(wait_random(max_delay)) for i in range(n)]

    # wait all missions and add result to list
    result = [await delay for delay in asyncio.as_completed(delays)]

    # Sort the list in ascending order
    result.sort()

    return result

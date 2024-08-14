#!/usr/bin/env python3
"""
this module import 'wait_random' from other file for display list of time wait
"""


import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    function return list 
    """
    delays = [asyncio.create_task(wait_random(max_delay)) for i in range(n)]
    result = [await delay for delay in asyncio.as_completed(delays)]

    return result

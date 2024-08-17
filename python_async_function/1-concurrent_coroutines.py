#!/usr/bin/env python3
"""
this module import 'wait_random' from other file for display list of time wait
"""


from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    function return list 
    """
    delay_list = []
    for x in range(n):
        delay = await wait_random(max_delay)
        delay_list.append(delay)
    return sorted(delay_list)

#!/usr/bin/env python3
"""
this module import 'wait_random'
"""


from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Return a list of delays in ascending order.

    Args:
        n (int): n times to call wait_random.
        max_delay (int): The maximum delay value.

    Returns:
        List[float]: A list of delay times
    """
    delay_list = []
    for x in range(n):
        delay = await wait_random(max_delay)
        delay_list.append(delay)
    return sorted(delay_list)

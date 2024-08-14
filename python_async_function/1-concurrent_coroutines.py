#!/usr/bin/env python3
"""Execute multiple coroutines"""

from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Async waits for 'n' random delays, return sorted list."""
    delay_list = []
    for i in range(n):
        delay = await wait_random(max_delay)
        delay_list.append(delay)
    return sorted(delay_list)

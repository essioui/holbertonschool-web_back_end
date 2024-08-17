#!/usr/bin/env python3
"""
Measure the runtime
"""


from typing import List
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure total execution time for 'wait_n'
      and returns average time per coroutine.

    Args:
        n (int): times to call the 'wait_n'.
        max_delay (int): The maximum delay .

    Returns:
        float: The average execution.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n

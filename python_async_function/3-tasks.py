#!/usr/bin/env python3
"""
create asyncio tasks
"""


import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    the regular function takes
    max_delay: int
    return: object asyncio.Task
    """
    return asyncio.create_task(wait_random(max_delay))

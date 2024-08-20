#!/usr/bin/env python3
"""
The coroutine will collect 10 random numbers
using an async comprehensing over async_generator,
then return the 10 random numbers
"""

async_generator = __import__('0-async_generator').async_generator
from typing import List
async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers using an async comprehension
    over async_generator, then returns the 10 random numbers.

    Returns:
        List[float]: A list of 10 random numbers.
    """
    return [number async for number in async_generator()]

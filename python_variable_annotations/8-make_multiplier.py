#!/usr/bin/env python3
"""
module have function `make_multiplier` return function `multiplier_function`
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    function have arg
    multiplier: float
    return function
    """
    def multiplier_function(value: float) -> float:
        """
        function have arg
        value: float
        return: float (multiplier * value)
        """
        return value * multiplier
    return multiplier_function

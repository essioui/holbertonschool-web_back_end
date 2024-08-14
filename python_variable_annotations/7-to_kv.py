#!/usr/bin/env python3
"""
this module write functio `to_kv` string and int/float to tuple
"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    function take two arg
    k: str
    v: union[int, float]
    return: tuple has two typles str and float
    """
    return k, float(v ** 2)

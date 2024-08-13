#!/usr/bin/env python3
"""
this module `sum_mixed_list` return list type float
"""


from typing import List, Union
def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    function has list with two type
    arg1: int
    arg2: float
    return list float
    """
    return float(sum(mxd_lst))

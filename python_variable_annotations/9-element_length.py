#!/usr/bin/env python3
"""
9-element_length.py
this module import Iterable, List, Tuple, Squence(not string any object)
"""

from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    function has arg
    lst: iterable and squence 
    return: squence and integer
    """
    return [(i, len(i)) for i in lst]

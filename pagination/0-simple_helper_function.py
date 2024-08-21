#!/usr/bin/env python3
"""
The function should return a tuple of size two containing
a start index and an end index corresponding to the range
of indexes to return in a list for those particular
pagination parameters.
"""


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """
    Returns a tuple containing the start index
    and end index for a given page
    and page_size.

    Args:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        tuple[int, int]: A tuple containing the start index and end index.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index

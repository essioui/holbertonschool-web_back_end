#!/usr/bin/env python3
"""
Module for pagination functionality.

Defines a function `index_range` for calculating the start and end index
for pagination and a `Server` class to handle data pagination from a CSV file.
"""

import csv
from typing import List, Tuple, Dict, Union
import math


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns a tuple containing the start index and end index for a given page
    and page_size.

    Args:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start index and end index.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index


class Server:
    """
    Server class to handle data pagination from a CSV file.

    Attributes:
        dataset (List[List[str]]): The data loaded from the CSV file.
    """

    def __init__(self):
        """
        Initialize the Server and load data from the CSV file.
        """
        self.dataset: List[List[str]] = []
        with open("Popular_Baby_Names.csv", "r") as file:
            reader = csv.reader(file)
            self.dataset = list(reader)[1:]

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List[str]]:
        """
        Retrieve a page of data from the dataset
        based on the page number and page size.

        Args:
            page (int): The page number (1-indexed). Default is 1.
            page_size (int): The number of items per page. Default is 10.

        Returns:
            List[List[str]]: The list of rows for the given page.
        """
        assert isinstance(page, int) and page > 0, (
            "Page number must be a positive integer"
        )
        assert isinstance(page_size, int) and page_size > 0, (
            "Page size must be a positive integer"
        )
        start_index, end_index = index_range(page, page_size)
        if start_index >= len(self.dataset):
            return []

        return self.dataset[start_index:end_index]

    def get_hyper(
            self, page: int = 1, page_size: int = 10
            ) -> Dict[str, Union[int, List[List[str]], None]]:
        """
        Retrieve pagination information including
        data for the current page, next page,
        previous page, and total pages.
        Args:
            page (int): The page number (1-indexed). Default is 1.
            page_size (int): The number of items per page. Default is 10.
        Returns:
            Dict[str, Union[int, List[List[str]], None]]:
                - page_size: The number of items per page.
                - page: The current page number.
                - data: The list of rows for the given page.
                - next_page: The page number of the next page
                or None if there is no next page.
                - prev_page: The page number of the previous
                page or None if there is no previous page.
                - total_pages: The total number of pages.
        """
        assert isinstance(page, int) and page > 0, (
            "Page number must be a positive integer"
        )
        assert isinstance(page_size, int) and page_size > 0, (
            "Page size must be a positive integer"
        )
        data = self.get_page(page, page_size)
        total_items = len(self.dataset)
        total_pages = math.ceil(total_items / page_size)
        prev_page = page - 1 if page > 1 else None
        next_page = page + 1 if page < total_pages else None
        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }

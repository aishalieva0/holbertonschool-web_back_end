#!/usr/bin/env python3
"""Simple helper function"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """return a tuple of size two containing a start index and an end index"""
    total = page * page_size
    start_index = total - page_size
    return (start_index, total)

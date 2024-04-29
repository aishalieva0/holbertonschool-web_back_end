#!/usr/bin/env python3
"""a type-annotated function sum_mixed_list"""

from typing import List


def sum_mixed_list(mxd_lst: List[int | float]) -> float:
    """returns their sum as a float"""
    return sum(mxd_lst)

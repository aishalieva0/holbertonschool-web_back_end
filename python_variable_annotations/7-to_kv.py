#!/usr/bin/env python3
"""a type-annotated function to_kv"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """returns a tuple"""
    return k, v * v

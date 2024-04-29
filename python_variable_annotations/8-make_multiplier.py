#!/usr/bin/env python3
"""a type-annotated function make_multiplier"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """multiplies a float"""

    def multiplier_func(f: float):
        return f * multiplier

    return multiplier_func

#!/usr/bin/env python3
"""Duck typing"""

from typing import Union, Sequence, Any, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """first element of a sequence"""
    if lst:
        return lst[0]
    else:
        return None

#!/usr/bin/env python3
"""iterable object"""

from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence[int]]) -> List[
        Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]


# typing.List[typing.Tuple[typing.Sequence, int]]}

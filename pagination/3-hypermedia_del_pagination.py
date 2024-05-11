#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))}
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """return a dictionary with key-value pairs

        Args:
            index (int): Defaults to None.
            page_size (int): Defaults to 10.

        Returns: Dict:
            index: first item in the current page.
            next_index: first item after the last item on the current page
            page_size: the current page size
            data: the actual page of the dataset
        """
        assert isinstance(index, int) and isinstance(page_size, int)
        assert 0 <= index < len(self.indexed_dataset())

        next_index = index + page_size
        page_data = []
        i = index
        while len(page_data) < page_size and i < next_index:
            if not self.indexed_dataset().get(i):
                next_index += 1
            else:
                page_data.append(self.indexed_dataset()[i])
            i += 1

        return {
            "index": index,
            "data": page_data,
            "page_size": page_size,
            "next_index": next_index,
        }

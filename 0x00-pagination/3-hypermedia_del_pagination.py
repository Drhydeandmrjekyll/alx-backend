#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate database of popular baby names."""
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
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Return hypermedia information for specified index.

        Args:
            index (int, optional): Index of first item in current page.
            Defaults to None.
            page_size (int, optional):
            Number of items per page. Defaults to 10.

        Returns:
            Dict: Hypermedia information.
        """
        indexed_dataset = self.indexed_dataset()

        if index is None:
            index = 0

        data = [indexed_dataset[i] for i in range(
            index,
            index + page_size
        ) if i in indexed_dataset]
        next_index = index + page_size

        if index not in indexed_dataset:
            return {
                "index": index,
                "data": [],
                "page_size": 0,
                "next_index": None
            }
        data = [indexed_dataset[i] for i in range(
            index,
            index + page_size
        ) if i in indexed_dataset]
        next_index = index + page_size

        return {
            "index": index,
            "data": data,
            "page_size": len(data),
            "next_index": next_index if next_index in indexed_dataset else None
        }


if __name__ == "__main__":
    server = Server()

    server.indexed_dataset()

    try:
        server.get_hyper_index(300000, 100)
    except AssertionError:
        print("AssertionError raised when out of range")

    index = 3
    page_size = 2

    print("Nb items: {}".format(len(server.indexed_dataset())))

    # 1- request first index
    res = server.get_hyper_index(index, page_size)
    print(res)

    # 2- request next index
    print(server.get_hyper_index(res.get('next_index'), page_size))

    # 3- remove the first index
    del server.indexed_dataset()[res.get('index')]
    print("Nb items: {}".format(len(server.indexed_dataset())))

    # 4- request initial index -> first data retrieve not same as first request
    print(server.get_hyper_index(index, page_size))

    # 5- request again initial next index -> same data page as request 2-
    print(server.get_hyper_index(res.get('next_index'), page_size))

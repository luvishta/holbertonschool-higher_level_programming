#!/usr/bin/python3
"""Module class for CountedIterator class"""


class CountedIterator:
    """The CountedIterator class"""

    def __init__(self, iterable):
        """Initialization with an iterable"""
        self.iterator = iter(iterable)
        self.counter = 0

    def __next__(self):
        """Overriding next method"""
        try:
            item = next(self.iterator)
            self.counter += 1
            return item

        except StopIteration:
            raise StopIteration

    def get_count(self):
        return self.counter


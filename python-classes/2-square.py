#!/usr/bin/python3
"""define the function"""


class Square:
    """A square class"""
    __size = None

    def __init__(self, size=0):
        """Initialize class"""
        if size is not int(size):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

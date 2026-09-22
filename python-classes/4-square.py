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

    def area(self):
        """Returns the current square area"""
        return (self.__size ** 2)

    @property
    def size(self):
        """To retrieve size"""
        return self.__size

    @size.setter
    def size(self, value):
        """To set size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

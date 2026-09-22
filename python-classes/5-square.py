#!/usr/bin/python3
"""define the function"""


class Square:
    """A square class"""

    def __init__(self, size=0):
        """Initialize class"""
        if size != int(size):
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

    def my_print(self):
        """Prints the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for int in range(self.__size):
                print("#" * self.__size)

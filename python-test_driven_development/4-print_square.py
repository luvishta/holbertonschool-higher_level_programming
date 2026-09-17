#!/usr/bin/python3

"""
    This module prints a square with the character #:
    print_square
"""


def print_square(size):
    """
    Prints a square with the character #.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size is float and size < 0:
        raise ValueError("size must be an integer")
    for i in range(size):
        print(size * "#")

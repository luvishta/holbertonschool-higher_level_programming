#!/usr/bin/python3
"""Define a function.

The add_integer function adds two integers.
It accepts integer or float arguments.
"""
def add_integer(a, b=98):
    """
        TypeError: If either of a or b is a non-integer and non-float.
    """
    if type(a) is not int and type(a) is not float:

        raise TypeError("a must be an integer")

    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    return int(a) + int(b)

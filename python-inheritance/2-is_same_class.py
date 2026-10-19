#!/usr/bin/python3

"""define the function"""


def is_same_class(obj, a_class):

    """returns True if the object is exactly an instance of the specified class
    otherwise False."""

    if type(obj) is a_class:
        return True
    elif type(obj) is not a_class:
        return False

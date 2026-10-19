#!/usr/bin/python3
"""define the module"""


def inherits_from(obj, a_class):
    """ returns True if the object is an instance of a class that inherited
    otherwise False."""
    return type(obj) is not a_class and isinstance(obj, a_class)

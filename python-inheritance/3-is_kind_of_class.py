#!/usr/bin/python3

"""define the function"""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance or inherited instance of a class.
    Returns:
        If obj is an instance or inherited- True.
        Otherwise - False."""
    if isinstance(obj, a_class):
        return True
    else:
        return False

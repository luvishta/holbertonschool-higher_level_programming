#!/usr/bin/python3
"""Module defines function class_to_json"""


def class_to_json(obj):
    """Returns the dictionary description of simple data structure
    (list, dictionary, string, integer, boolean)

    Return the dictionary of given object
        obj: instance of a class
    """
    return obj.__dict__

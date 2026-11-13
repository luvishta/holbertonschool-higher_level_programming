#!/usr/bin/python3
"""Defines a function that a serialzed string"""
import json


def to_json_string(my_obj):
    """Function returns object from JSON string
    having
        my_str: JSON string
    Return:
        Returns python object
    """
    return json.loads(my_obj)

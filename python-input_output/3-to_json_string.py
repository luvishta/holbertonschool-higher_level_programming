#!/usr/bin/python3
"""Defines a function that a serialzed string"""
import json


def to_json_string(my_obj):
    """function returns JSON representation of object
    having
        my_obj: object to serialize
     and return
        serialized object
    """

    return json.dumps(my_obj)

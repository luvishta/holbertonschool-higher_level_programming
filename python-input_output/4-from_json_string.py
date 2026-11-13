#!/usr/bin/python3
"""Defines a function that a serialzed string"""
import json


def to_json_string(my_obj):
    """function returns JSON representation of object

    return json string to python 
    """
    return json.loads(my_obj)

#!/usr/bin/python3
"""Defines a function that a serialzed string"""
import json


def to_json_string(my_obj):
    
    """Convert a JSON string to a Python object."""
    return json.loads(my_obj)

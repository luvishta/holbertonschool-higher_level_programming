#!/usr/bin/python3
"""Defines functions that serialize and deserialize data"""
import json


def serialize_and_save_to_file(data, filename):
    """Function serializes data to JSON with
        filename: File name of JSON file
    """

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Function desirializes JSON data into python dictionery with
        filename: file to read data from
    """
    with open(filename, "r", encoding="utf-8") as f:
        dictionery = json.load(f)
    return dictionery

#!/usr/bin/python3
"""Module creates class Student"""


class Student:
    """Student class with public instance attributes

    Instance Attributes:
        first_name: first name ofs the tudent
        last_name: last name of the student
        age: age of student
    """

    def __init__(self, first_name, last_name, age):
        """Instantiates public instance attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns dictionary representation of instance
            attrs: attributes to retrieve.
            if not a list of strings, retrieve all attributes
        """
        if type(attrs) is not list:
            return self.__dict__
        filtered = {}
        for a in attrs:
            if type(a) is not str:
                return self.__dict__
            value = getattr(self, a, None)
            if value is None:
                continue
            filtered[a] = value
        return filtered

    def reload_from_json(self, json):
        """Replace all attributes of instance with those in json
            json: dictionary with attributes to use
        """
        for key, value in json.items():
            self.__dict__[key] = value

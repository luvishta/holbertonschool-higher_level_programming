#!/usr/bin/python3
"""Module containing Dragon class"""


class SwimMixin:
    """The SwimMixin class"""
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """The FlyMixin class"""
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """The Dragon class"""
    def roar(self):
        print("The dragon roars!")

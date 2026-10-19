#!/usr/bin/python3
"""Defines an inherited list class MyList."""


class MyList(list):
    """ the built-in list class for printing."""

    def print_sorted(self):
        """Print a list in sorted in the ascending order."""
        print(sorted(self))

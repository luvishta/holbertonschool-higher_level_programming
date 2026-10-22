#!/usr/bin/python3
"""Module containing  the VerboseList class"""


class VerboseList(list):
    """List class that prints msg"""

    def append(self, value):
        """Add an item to the list"""
        print(f"Added [{value}] to the list.")
        list.append(self, value)

    def extend(self, value):
        """Add multiple items in the list"""
        print(f"Extended the list with [{len(value)}] items.")
        list.extend(self, value)

    def remove(self, value):
        """Remove an item from the list"""
        list.remove(self, value)
        print(f"Removed [{value}] from the list.")

    def pop(self, value=None):
        """Pop method"""

    def pop(self, index=-1):
        """Remove and return an item from the list"""
        item = list.pop(self, index)
        print(f"Popped [{item}] from the list.")
        return item
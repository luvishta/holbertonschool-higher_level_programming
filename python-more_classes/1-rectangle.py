#!/usr/bin/python3
"""define the function"""


class Rectangle:
    """Class representing rectangle"""

    def __init__(self, width=0, height=0):
        """initialization of the instance"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @property
    def height(self):
        """Getter for __height"""
        return self.__height

    @width.setter
    def width(self, value):
        """Setter for width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Setter for height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

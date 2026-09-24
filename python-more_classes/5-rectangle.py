#!/usr/bin/python3
"""Module defining Rectangle class"""


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

    def area(self):
        """Method to calculate area"""
        return self.__height * self.__width

    def perimeter(self):
        """Method to calculate perimeter"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        if self.__height == 0 or self.width == 0:
            return ("")

        rect = []

        for i in range(self.height):
            rect.append("#" * self.width)

        return "\n".join(rect)

    def __repr__(self):
        if self.__height == 0 or self.width == 0:
            return ("")
        else:
            return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        print("Bye rectangle...")

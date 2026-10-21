#!/usr/bin/python3
"""module having the class """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class based on Rectangle class"""

    def __init__(self, size):
        """Initialising for the Square object"""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return ("[Square] {}/{}".format(self.__size, self.__size))

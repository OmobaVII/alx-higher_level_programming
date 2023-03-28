#!/usr/bin/python3
"""
Module: 4-square
define a square
"""


class Square:
    """
    definition of square
    """
    def __init__(self, size=0):
        self.size = size

        """
        gives a private instance attribute for size
        """
    @property
    def size(self):
        return self.__size

    """
    the property setter for the attribute
    """
    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """
    returns the area of the square
    """
    def area(self):
        return (self.__size ** 2)

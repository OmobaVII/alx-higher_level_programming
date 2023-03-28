#!/usr/bin/python3
"""
Module: 3-square
defines a class Square
"""


class Square:
    """
    definition of a class named Square
    """
    def __init__(self, size=0):
        """
        initializes the square with a size
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        returns the area of the square
        """
        return (self.__size ** 2)

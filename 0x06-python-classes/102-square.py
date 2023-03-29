#!/usr/bin/python3
"""
Module: 102-square
defines class square
"""


class Square:
    """
    the definition of the square
    """
    def __init__(self, size=0):
        """
        the initialization of the square
        """
        self.__size = size

    @property
    def size(self):
        """
        gets the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        sets the size of the square
        """
        if type(value) != int or type(value) != float:
            raise TypeError("size must be a number")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        returns the area of the square
        """
        return (self.__size ** 2)

    def __eq__(self, another):
        """
        because of the == comparism
        """
        return self.__size == another.size

    def __ne__(self, another):
        """
        because of the != comparism
        """
        return self.__size != another.size

    def __gt__(self, another):
        """
        because of the > comparism
        """
        return self.__size > another.size

    def __ge__(self, another):
        """
        because of the greater than or equal
        comparism
        """
        return self.__size >= another.size

    def __lt__(self, another):
        """
        because of the less than comparism
        """
        return self.__size < another.size

    def __le__(self, another):
        """
        because of the less than or equal
        comparism
        """
        return self.__size <= another.size

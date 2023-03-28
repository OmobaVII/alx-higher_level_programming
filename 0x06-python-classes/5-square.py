#!/usr/bin/python3
"""
Module: 5-square
defines a class Square
"""


class Square:
    """
    the definition of the class
    """

    def __init__(self, size=0):
        self.size = size

    """
    gets the property size
    """
    @property
    def size(self):
        return self.__size

    """
    sets the size attribute
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

    """
    prints the square itself using #
    """
    def my_print(self):
        a = 0
        b = 0
        if self.__size > 0:
            while b < self.__size:
                while a < self.__size:
                    print("#", end="")
                    a = a + 1
                b = b + 1
                a = 0
                print()
        if self.__size == 0:
            print()

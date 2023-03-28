#!/usr/bin/python3
"""
Module: 6-square
defines a class square
"""


class Square:
    """
    definition of the class
    """

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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
    gets the property position
    """
    @property
    def position(self):
        return self.__position

    """
    sets the position of the attribute
    """
    @position.setter
    def position(self, value):
        if type(value) != tuple or type(value[0]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    """
    returns the area of the square
    """
    def area(self):
        return (self.__size ** 2)

    """
    prints the square using #
    """
    def my_print(self):
        a = 0
        b = 0
        position = list(self.__position)
        while b < self.__size:
            while position[1] > 0:
                print()
                position[1] -= 1
            while position[0] > 0:
                print(" ", end="")
                position[0] -= 1
            while a < self.__size:
                print("#", end="")
                a = a + 1
            a = 0
            b = b + 1
            position[0] = self.__position[0]
            print()
        if self.__size == 0:
            print()

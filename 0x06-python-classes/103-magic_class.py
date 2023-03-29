#!/usr/bin/python3

"""
Module: 103-magic_class
defines a class MagicClass
"""


import math


class MagicClass:
    """
    definition of the class
    """
    def __init__(self, radius):
        if type(radius) is not int:
            raise TypeError("radius must be a number")
        if type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        return 2 * math.pi * self.__radius

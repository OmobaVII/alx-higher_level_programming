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
    def __init__(self, radius=0):
        self.radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        if type(value) is not int and type(value) is not float:
            raise TypeError('radius must be a number')
        self.__radius = value

    def area(self):
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        return 2 * math.pi * self.__radius

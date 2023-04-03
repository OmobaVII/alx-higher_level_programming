#!/usr/bin/python3
"""
This is the 1-rectangle Module
This module defines a class rectangle
The class Rectangle is made up of width and value
"""


class Rectangle:
    """
    defines the class rectangle
    the rectangle has both the width
    and height attribute
    """
    def __init__(self, width=0, height=0):
        """
        gives and attribute width to the rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        retrieves the private
        instance attribute
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        sets the width of the rectangle
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        retrives the private instance attribute
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        sets the height of the rectangle
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

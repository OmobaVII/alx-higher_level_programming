#!/usr/bin/python3
"""
this is the 2-rectangle module
This module defines a class Rectangle
This module provides up to the area of the rectangle
"""


class Rectangle:
    """
    this is the definition of the class
    rectangle
    """
    def __init__(self, width=0, height=0):
        """
        definition of the parameters width and height
        for the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ define the property width """
        return self.__width

    @width.setter
    def width(self, value):
        """sets the propety width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ retrieves this height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the property height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ returns the area of the rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            perimeter = 0
        perimeter = 2 * (self.__height + self.__width)
        return perimeter

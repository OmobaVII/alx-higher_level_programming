#!/usr/bin/python3
"""
this is the 3-rectangle Module
this module provides the class Rectangle
the rectangle has two attributes width and height
"""


class Rectangle:
    """defines the class"""

    def __init__(self, width=0, height=0):
        """
        this defines the attribute of width and height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        retrieves the width of the rectangle
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
        retrieves the height of the rectangle
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

    def area(self):
        """ returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """ returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        a = 0
        b = 0
        s = ""
        if self.__width == 0 or self.__height == 0:
            return s
        while b < self.__height:
            while a < self.width:
                s += "#"
                a += 1
            b += 1
            a = 0
            if b < self.__height:
                s += "\n"
        return s


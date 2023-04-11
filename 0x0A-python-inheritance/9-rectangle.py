#!/usr/bin/python3
"""
This is the "9-rectangle' Module
this module provides a class called Rectangle
which inherits from BaseGeomtry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""imports the supper class BaseGeometry"""


class Rectangle(BaseGeometry):
    """defines the class Rectangle"""
    def __init__(self, width, height):
        """initializes the rectangle with width and height
        and validates them with integer_validator"""

        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """returns the area"""
        return self.__width * self.__height

    def __str__(self):
        s = ""
        s += "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
        return s

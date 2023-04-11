#!/usr/bin/python3
"""
this is the `8-rectangle' module
This module has just two classes
BaseGeometry() and Rectangle which is a sub
class of BaseGeometry
"""


class BaseGeometry:
    """defines a class called BaseGeometry"""
    def area(self):
        """raise an exception with a message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """defines a class Rectangle which is a subclass of BaseGeometry"""
    def __init__(self, width, height):
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

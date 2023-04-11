#!/usr/bin/python3
"""
this is the `8-rectangle' module
This module has just two classes
BaseGeometry() and Rectangle which is a sub
class of BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
imports the super class
"""


class Rectangle(BaseGeometry):
    """defines a class Rectangle which is a subclass of BaseGeometry"""
    def __init__(self, width, height):
        """validates and initializes width and height"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

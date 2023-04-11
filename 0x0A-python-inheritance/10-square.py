#!/usr/bin/python3
"""
this is the '10-square' module
This module defines a class square
Square is a subclass of Rectangle
"""


Rectangle = __import__('9-rectangle').Rectangle
"""imports the Rectangle class"""


class Square(Rectangle):
    """defines the class Square which is a sub class of rectangle"""
    def __init__(self, size):
        """initializes the rectangle with size"""
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

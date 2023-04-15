#!/usr/bin/python3
"""
this is the `rectangle` module
it inherits from Base in the `base` module
this module defines a class Rectangle
"""

from models.base import Base
"""this imports the base module"""


class Rectangle(Base):
    """defines the class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """intializes the class with these parameters"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

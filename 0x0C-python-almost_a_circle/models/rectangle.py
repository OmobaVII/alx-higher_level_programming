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
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """retrieves the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the value of width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """retrieves the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the value of the height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """retrives the value of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets the value of x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """retrieves the value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets the value of y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """prints the rectangle"""
        a = 0
        b = 0
        x = self.__x
        y = self.__y
        while a < self.__height:
            while b < self.__width:
                while y > 0:
                    print()
                    y -= 1
                while x > 0:
                    print(" ", end="")
                    x -= 1    
                print("#", end="")
                b += 1
            a += 1
            b = 0
            x = self.__x
            print()

    def __str__(self):
        """returns a format of rectanlge, id x, y and width, height"""
        ms = "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}"
        s = ms.format(self.id, self.__x, self.__y, self.__width, self.__height)
        return s

    def update(self, *args, **kwargs):
        if args:
            attrs = ['id', 'width', 'height', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        s = {}
        s['id'] = self.id
        s['width'] = self.__width
        s['height'] = self.__height
        s['x'] = self.__x
        s['y'] = self.__y
        return s

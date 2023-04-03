#!/usr/bin/python3
"""
this is the 9-rectangle Module
this module provides the class Rectangle
the rectangle has two attributes width and height
"""


class Rectangle:
    """defines the class"""

    number_of_instances = 0
    print_symbol = None

    def __init__(self, width=0, height=0):
        """
        this defines the attribute of width and height
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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

    print_symbol = "#"

    def __str__(self):
        a = 0
        b = 0
        s = ""
        if self.__width == 0 or self.__height == 0:
            return s
        while b < self.__height:
            while a < self.width:
                s += "{}".format(self.print_symbol)
                a += 1
            b += 1
            a = 0
            if b < self.__height:
                s += "\n"
        return s

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if (rect_1.width * rect_1.height) >= (rect_2.width * rect_2.height):
            return rect_1
        else:
            return rect_2
    @classmethod
    def square(cls, size=0):
        return cls(size, size)

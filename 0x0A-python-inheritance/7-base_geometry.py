#!/usr/bin/python3
"""
this is the `7-base_geometry' module
This module has just one class
BaseGeometry()
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

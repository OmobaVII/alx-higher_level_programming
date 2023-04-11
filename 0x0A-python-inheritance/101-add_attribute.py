#!/usr/bin/python3
"""
This is the 101-add_attribute Module
This module provide one function
add_attribute()
"""


def add_attribute(obj, attribute_name, value):
    """the function that adds a new attribute to an object if possible"""
    if hasattr(obj, '__dict__'):
        setattr(obj, attribute_name, value)
    else:
        raise TypeError("can't add new attribute")

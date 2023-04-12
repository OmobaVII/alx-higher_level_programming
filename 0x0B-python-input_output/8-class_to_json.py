#!/usr/bin/python3
"""
the 8-class_to_json module
this module provides one function
class_to_json()
"""


def class_to_json(obj):
    """returns the dictionary description"""

    s = obj.__dict__
    return s

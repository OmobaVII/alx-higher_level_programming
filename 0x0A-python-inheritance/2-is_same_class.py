#!/usr/bin/python3
"""
the module `2-is_same_class`
this module defines just 1 function
"""


def is_same_class(obj, a_class):
    """returns True is isinstance"""

    if type(obj) is a_class:
        return True
    else:
        return False

#!/usr/bin/python3
"""
this is the `3-is_kind_of_class` Module
this module defines just one function
"""


def is_kind_of_class(obj, a_class):
    """Returns True is obj is an instance or class of a_class"""
    if isinstance(obj, a_class):
        return True
    else:
        return False

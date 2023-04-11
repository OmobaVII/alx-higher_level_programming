#!/usr/bin/python3
"""
this is the `4-inherits_from` module
this module provide just one function
"""


def inherits_from(obj, a_class):
    """returns True if an instance of a obj
    is inherited(directly or indirectly)
    from a_class"""

    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False

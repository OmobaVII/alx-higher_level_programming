#!/usr/bin/python3
"""
the '0-lookup' module
this module defines just one function
"""


def lookup(obj):
    """a function that returns the list of available attributes"""
    return dir(obj)

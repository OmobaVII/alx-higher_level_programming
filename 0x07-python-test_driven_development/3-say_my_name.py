#!/usr/bin/python3
"""
This is the "3-say_my_name" module.
This module supplies one function, say_my_name()
This function take in two strings and returns the joined strings
"""


def say_my_name(first_name, last_name=""):
    """
    Returns a combination of first_name and last_name
    """
    if type(first_name) not in [str]:
        raise TypeError("first_name must be a string")
    if type(last_name) not in [str]:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))

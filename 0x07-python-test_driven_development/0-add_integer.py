#!/usr/bin/python3
"""
This is the "0-add_integer" module.
The 0-add_integer module supplies one function, add_integer().
This function accepts two values, cast them to int and return the sum.

"""


def add_integer(a, b=98):
    """
    Returns the sum of a and b as int
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)

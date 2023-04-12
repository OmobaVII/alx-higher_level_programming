#!/usr/bin/python3
"""
this is the 12-pascal_triangle module
this module provides one function
pascal_triangle()
"""


def pascal_triangle(n):
    """a function that returns the pascal triangle of n"""

    s = []
    if n <= 0:
        return s
    for num in range(n):
        s.append(str(11 ** num))
    return s

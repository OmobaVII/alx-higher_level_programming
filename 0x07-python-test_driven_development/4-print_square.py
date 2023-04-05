#!/usr/bin/python3
"""
This is the module "4-print_square"
This module take in one function, print_square()
This function takes one parameter used as the size of a square to print using #
"""


def print_square(size):
    """prints a square using the character '#'"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    a = 0
    b = 0
    while a < size:
        while b < size:
            print("#", end="")
            b += 1
        b = 0
        a += 1
        print()

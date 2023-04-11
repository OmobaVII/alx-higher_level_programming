#!/usr/bin/python3
"""
this is the 1-my_list module
This module defines a class
MyList
"""


class MyList(list):
    """defines the class"""

    def __init__(self):
        """initializes the list"""
        super().__init__()

    def print_sorted(self):
        """a public instance attribute"""
        sorted_list = sorted(self)
        print(sorted_list)

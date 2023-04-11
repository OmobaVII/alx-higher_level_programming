#!/usr/bin/python3
"""
this is the 1-my_list module
This module defines a class
MyList
"""


class MyList(list):
    """defines the class"""

    def print_sorted(self):
        """a public instance attribute"""
        print(sorted(self))

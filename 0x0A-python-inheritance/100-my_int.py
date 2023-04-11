#!/usr/bin/python3
"""
This is the 100-my_int module
This module defines one class MyInt
MyInt is a sub class of int
"""


class MyInt(int):
    """defines the class"""
    def __eq__(self, another):
        """switches != and =="""
        return int(self) != int(another)

    def __ne__(self, another):
        """switches == and !="""
        return int(self) == int(another)

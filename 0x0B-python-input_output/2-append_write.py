#!/usr/bin/python3
"""
this is the 2-append_write module
This module provides one function
append_write()
"""


def append_write(filename="", text=""):
    """this function appends to the end of
    a file and returns the number of characters added"""

    with open(filename, "a", encoding="utf-8") as myFile:
        return myFile.write(text)

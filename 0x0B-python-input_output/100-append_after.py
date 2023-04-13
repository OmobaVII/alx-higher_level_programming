#!/usr/bin/python3
"""
this is the `100-append_after` module
this module provides one function
append_after()
"""


def append_after(filename="", search_string="", new_string=""):
    """searchs for a string and inserts a newstring after the line"""

    with open(filename, "r") as myFile:
        lines = myFile.readlines()

    with open(filename, "w") as myFile:
        for line in lines:
            myFile.write(line)
            if search_string in line:
                myFile.write(new_string)

#!/usr/bin/python3
"""
this is the 1-write_file module
this module provides one function
write_file()
"""


def write_file(filename="", text=""):
    """this function writes a string to a text file"""

    with open(filename, "w", encoding="utf-8") as myFile:
        return myFile.write(text)

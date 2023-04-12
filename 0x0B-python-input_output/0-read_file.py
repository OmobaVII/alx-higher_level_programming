#!/usr/bin/python3
"""
this is the 0-read_file module
this module provides one function
read_file()
"""


def read_file(filename=""):
    """reads the file and prints it to stdout"""

    with open(filename, "r", encoding="utf-8") as myFile:
        print(myFile.read(), end="")

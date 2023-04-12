#!/usr/bin/python3
"""
this is the 6-load_from_json_file module
this module provides one function
load_from_json_file()
"""


import json
"""this is the module important for the json"""


def load_from_json_file(filename):
    """creates an Object from a JSON file"""

    with open(filename, "r", encoding="utf-8") as myFile:
        return json.load(myFile)

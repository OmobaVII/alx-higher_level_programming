#!/usr/bin/python3
"""
this is the 5-save_to_json_file module
this module provides one function
save_to_json_file()
"""


import json
"""this is the json module needed for the function"""


def save_to_json_file(my_obj, filename):
    """writes an object to a text file using json rep"""

    with open(filename, "w", encoding="utf-8") as myFile:
        return json.dump(my_obj, myFile)

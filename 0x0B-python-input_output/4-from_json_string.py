#!/usr/bin/python3
"""
this is the 4-from_json_string module
this module provides one function
from_json_string
"""


import json
"""this is the json module needed"""


def from_json_string(my_str):
    """deserializing a string"""

    obj = json.loads(my_str)
    return obj

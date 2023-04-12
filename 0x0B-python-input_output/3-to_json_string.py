#!/usr/bin/python3
"""
this is the 3-to_json_string module
this module provides just one function
to_json_string()
"""


import json
"""needed to return the json representation of an object"""


def to_json_string(my_obj):
    """returns a json representation of an object"""
    s = json.dumps(my_obj)
    return s

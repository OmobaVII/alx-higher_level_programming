#!/usr/bin/python3
"""
the 8-class_to_json module
this module provides one function
class_to_json()
"""


import json
"""module important for json to run"""


def class_to_json(obj):
    """returns the dictionary description"""

    s = json.dumps(obj, default=lambda x: x.__dict__)
    return s

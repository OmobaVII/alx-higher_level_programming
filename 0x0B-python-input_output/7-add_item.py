#!/usr/bin/python3
"""
this it the 7-add_item module
this module adds all arguments to a python list
"""

from sys import argv
"""imports the module needed to get arguments"""


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
"""imports the function save_to_json_file"""

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
"""imports the function load_from_json_file"""

myFile = "add_item.json"

try:
    file_content = load_from_json_file(myFile)
except Exception:
    file_content = []

save_to_json_file(file_content + argv[1:], myFile)

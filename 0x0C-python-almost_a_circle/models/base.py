#!/usr/bin/python3
"""
this is the `base` module
this module provides a class called
Base
"""


class Base:
    """the definition of the class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initialization of  id"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns a string representation"""
        import json
        """needed to returns json representation"""
        s = "[]"
        if list_dictionaries is None:
            return s
        if len(list_dictionaries) == 0:
            return s
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes json to file"""
        import json
        filename = cls.__name__+".json"
        if list_objs is None:
            list_objs = []
        with open(filename, "w", encoding="utf8") as myFile:
            myFile.write(cls.to_json_string([obj.to_dictionary()
                         for obj in list_objs]))

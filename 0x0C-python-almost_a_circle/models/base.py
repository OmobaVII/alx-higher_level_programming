#!/usr/bin/python3
"""
this is the `base` module
this module provides a class called
Base
"""


import json
import csv
"""needed for the csv files"""


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

        s = "[]"
        if list_dictionaries is None:
            return s
        if len(list_dictionaries) == 0:
            return s
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes json to file"""

        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []
        with open(filename, "w", encoding="utf8") as myFile:
            myFile.write(cls.to_json_string([obj.to_dictionary()
                         for obj in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """returns the string from JSON"""
        if json_string is None:
            json_string = "[]"
        if len(json_string) == 0:
            json_string = "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls()

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__+".json"
        try:
            with open(filename, "r") as myFile:
                string = myFile.read()
        except FileNotFoundError:
            return []

        object_list = cls.from_json_string(string)
        return [cls.create(**obj) for obj in object_list]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serialize to CSV"""
        filename = cls.__name__+".csv"
        if list_objs is None:
            list_objs = []
        with open(filename, "w", newline="") as myFile:
            for obj in list_objs:
                wr = csv.writer(myFile)
                if cls.__name__ == "Rectangle":
                    wr.writerow([obj.id, obj.width, obj.height, obj.x, obj.y])
                elif cls.__name__ == "Square":
                    wr.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """deserialize from csv"""
        instances = []
        filename = cls.__name__ + ".csv"

        with open(filename, "r", newline="") as myFile:
            reader = csv.reader(myFile)
            for row in reader:
                if cls.__name__ == "Rectangle":
                    instance = {"id": int(row[0]),
                                "width": int(row[1]),
                                "height": int(row[2]),
                                "x": int(row[3]),
                                "y": int(row[4])}
                elif cls.__name__ == "Square":
                    instance = {"id": int(row[0]),
                                "size": int(row[1]),
                                "x": int(row[2]),
                                "y": int(row[3])}
                diction = cls.create(**instance)
                instances.append(diction)
        return instances

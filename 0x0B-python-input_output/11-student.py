#!/usr/bin/python3
"""
this is the 11-student module
this module defines a class based on 10-student module
"""


class Student:
    """defines the class"""

    def __init__(self, first_name, last_name, age):
        """initializes these instances"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation"""
        if attrs is None:
            return self.__dict__
        mydictionary = dict()
        for a in attrs:
            if a in self.__dict__.keys():
                mydictionary[a] = self.__dict__[a]
        return mydictionary

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        self.first_name = json.get("first_name", self.first_name)
        self.last_name = json.get("last_name", self.last_name)
        self.age = json.get("age", self.age)

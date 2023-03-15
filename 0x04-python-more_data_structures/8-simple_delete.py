#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    for a in list(a_dictionary):
        if a == key:
            del a_dictionary[key]
    return (a_dictionary)

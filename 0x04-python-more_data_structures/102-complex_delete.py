#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for a in list(a_dictionary.keys()):
        if a_dictionary[a] == value:
            del a_dictionary[a]
    return (a_dictionary)

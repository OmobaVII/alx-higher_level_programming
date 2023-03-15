#!/usr/bin/python3
def best_score(a_dictionary):
    if (a_dictionary):
        new_dictionary = {}
        sort = sorted(a_dictionary.items(), key=lambda a: a[1], reverse=True)
        new_dictionary.update(sort)
        for a, b in new_dictionary.items():
            return (a)
            break

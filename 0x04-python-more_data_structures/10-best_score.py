#!/usr/bin/python3
def best_score(a_dictionary):
    if (a_dictionary):
        new_dictionary = {}
        new_dictionary.update(sorted(a_dictionary.items(), key=lambda a:a[1], reverse=True))
        for a, b in new_dictionary.items():
            return (a)
            break

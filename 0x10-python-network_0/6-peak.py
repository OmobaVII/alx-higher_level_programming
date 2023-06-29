#!/usr/bin/python3
"""
this Modele defines a function that
finds a peak in a list of unsorted
integers
"""


def find_peak(list_of_integers):
    """definition of the function"""
    if list_of_integers is None:
        return None

    if len(list_of_integers) < 1:
        return None

    peak = list_of_integers[0]

    for num in list_of_integers:
        if num > peak:
            peak = num

    return peak

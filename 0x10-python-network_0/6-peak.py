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

    ilist = list_of_integers
    end = len(ilist) - 1
    middle = end // 2

    if ilist[0] >= ilist[1]:
        return ilist[0]
    if ilist[end] >= ilist[end - 1]:
        return ilist[end]

    if ilist[middle] < ilist[middle - 1]:
        return find_peak(ilist[:middle + 1])
    elif ilist[middle] < ilist[middle + 1]:
        return find_peak(ilist[middle:])
    else:
        return ilist[middle]

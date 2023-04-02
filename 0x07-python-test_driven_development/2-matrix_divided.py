#!/usr/bin/python3
"""
This is the "2-matrix_divided" module.
This module supplies one function, matrix_divided().
This function accepts two values, returns the matrix divided.
"""


def matrix_divided(matrix, div):
    """
    Returns the matrix divided by div
    """
    message = "matrix must be a matrix (list of lists) of integers/floats"
    for items in matrix:
        for a in items:
            if type(a) not in [int, float]:
                raise TypeError(message)
    row_len = len(matrix[0])
    for item in matrix:
        if len(item) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for lists in matrix:
        new_matrix.append(list(map(lambda x: round((x / div), 2), lists)))
    return (new_matrix)

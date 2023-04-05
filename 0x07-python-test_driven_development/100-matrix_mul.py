#!/usr/bin/python3
"""
the 100-matrix_mul module
this module provides one function, matrix_mul.
this function takes two matrix as arguments and return thier product
"""


def matrix_mul(m_a, m_b):
    """
    returns the product of matrix m_a and matrix m_b
    """
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    for lists_a in m_a:
        if type(lists_a) is not list:
            raise TypeError("m_a must be a list of lists")
    for lists_b in m_b:
        if type(lists_b) is not list:
            raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    for list_a in m_a:
        for i in list_a:
            if type(i) not in [int, float]:
                raise TypeError("m_a should contain only integers or floats")
    for list_b in m_b:
        for j in list_b:
            if type(j) not in [int, float]:
                raise TypeError("m_b should contain only integers or floats")
    col_a = len(m_a[0])
    for items in m_a:
        if len(items) != col_a:
            raise TypeError("each row of m_a must be of the same size")
    col_b = len(m_b[0])
    for item in m_b:
        if len(item) != col_b:
            raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    row_a = len(m_a)
    row_b = len(m_b)
    new_matrix = [[0 for a in range(col_b)] for b in range(row_a)]
    for x in range(row_a):
        for y in range(col_b):
            for z in range(col_a):
                new_matrix[x][y] += m_a[x][z] * m_b[z][y]
    return new_matrix

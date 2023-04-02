#!/usr/bin/python3
import numpy as np
"""
this is the "101-lazy_matrix_mul" module
this module provide one function, lazy_matrix_mul()
this function takes in two matrix as parameter and returns thier product
"""
def lazy_matrix_mul(m_a, m_b):
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
    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0:
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
    row_a = len(m_a)
    row_b = len(m_b)
    if row_a != col_b and row_b != col_a:
        raise ValueError("m_a and m_b can't be multiplied")
    new_matrix = [[]]
    new_matrix = np.dot(m_a, m_b)
    return new_matrix

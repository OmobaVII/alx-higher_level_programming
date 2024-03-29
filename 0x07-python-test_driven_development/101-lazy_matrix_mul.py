#!/usr/bin/python3
"""
imports the numpy module
"""
import numpy as np
"""
this is the "101-lazy_matrix_mul" module
this module provide one function, lazy_matrix_mul()
this function takes in two matrix as parameter and returns thier product
"""


def lazy_matrix_mul(m_a, m_b):
    """multiplies the matrix with numpy"""
    if type(m_a) is not list:
        raise TypeError("Scalar operands are not allowed, use '*' instead")
    if type(m_b) is not list:
        raise TypeError("Scalar operands are not allowed, use '*' instead")
    for lists_a in m_a:
        if type(lists_a) is not list:
            raise TypeError("m_a must be a list of lists")
    for lists_b in m_b:
        if type(lists_b) is not list:
            raise TypeError("m_b must be a list of lists")
    for list_a in m_a:
        for i in list_a:
            if type(i) not in [int, float]:
                raise TypeError("invalid data type for einsum")
    for list_b in m_b:
        for j in list_b:
            if type(j) not in [int, float]:
                raise TypeError("invalid data type for einsum")
    if len(m_a) == 0:
        col_a = 0
    else:
        col_a = len(m_a[0])
    for items in m_a:
        if len(items) != col_a:
            raise TypeError("setting an array element with a sequence.")
    if len(m_b) == 0:
        col_b = 0
    else:
        col_b = len(m_b[0])
    for item in m_b:
        if len(item) != col_b:
            raise TypeError("setting an array element with a sequence.")
    row_a = len(m_a)
    row_b = len(m_b)
    msg = ("shapes ({:d},{:d}) and ({:d},{:d}) not aligned: "
           "{:d} (dim {:d}) != {:d} (dim {:d})"
           .format(col_b, row_a, col_b, col_b, row_a, row_b, col_b, row_a))
    if col_a != row_b and col_b != row_a:
        raise ValueError(msg)
    new_matrix = [[]]
    new_matrix = np.matmul(m_a, m_b)
    return new_matrix

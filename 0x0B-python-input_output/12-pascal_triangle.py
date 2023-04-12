#!/usr/bin/python3
"""
this is the 12-pascal_triangle module
this module provides one function
pascal_triangle()
"""


def pascal_triangle(n):
    """a function that returns the pascal triangle of n"""

    triangle = []
    for a in range(n):
        row = [1] * (a + 1)
        for b in range(1, a):
            row[b] = triangle[a - 1][b - 1] + triangle[a - 1][b]
        triangle.append(row)

    return triangle

#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for a in matrix:
        for i, j in enumerate(a):
            if i < len(a) - 1:
                print("{:d}".format(j), end=" ")
            else:
                print("{:d}".format(j), end="")
        print("")

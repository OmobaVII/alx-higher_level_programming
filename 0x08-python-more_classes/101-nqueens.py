#!/usr/bin/python3
"""
this module provides a function that
solves the N queens puzzle
"""


import sys


def nqueens(number):
    if type(number) is not int:
        print("N must be a number")
        sys.exit(1)
    if number < 4:
        print("N must be at least 4")
        sys.exit(1)

    answer = []

    def backtrack(queen, sum_of_row_col, diff_of_row_col):
        row = len(queen)
        if row == number:
            answer.append(queen.copy())
            return

        for col in range(number):
            if col not in queen\
                    and row + col not in sum_of_row_col\
                    and row - col not in diff_of_row_col:
                backtrack(queen + [col], sum_of_row_col + [row + col],
                          diff_of_row_col + [row - col])

    backtrack([], [], [])

    for queens in answer:
        print([[i, queens[i]] for i in range(number)])


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        number = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    nqueens(number)

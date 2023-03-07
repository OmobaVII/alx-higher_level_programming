#!/usr/bin/python3
def print_last_digit(number):
    number = abs(number)
    n = int(number % 10)
    print("{0}".format(n), end="")
    return (n)

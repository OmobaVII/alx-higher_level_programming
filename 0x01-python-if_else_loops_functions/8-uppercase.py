#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if i >= 'a' and i <= 'z':
            i = chr(ord(i) - 32)
        else:
            i = i
        print("{0}".format(i), end="")
    print("")

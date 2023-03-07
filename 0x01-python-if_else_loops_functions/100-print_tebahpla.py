#!/usr/bin/python3
for i in range(ord('z'), ord('a')-1, -1):
    if (i % 2) == 1:
        i = i - 32
    else:
        i = i
    i = chr(i)
    print("{0}".format(i), end="")

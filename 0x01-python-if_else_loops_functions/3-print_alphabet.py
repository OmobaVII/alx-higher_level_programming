#!/usr/bin/python3
for i in range(97, 122):
    if i == 101 or i == 113:
        continue
    else:
        print("{0:c}".format(i), end="")

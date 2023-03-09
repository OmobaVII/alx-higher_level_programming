#!/usr/bin/python3
import sys
if len(sys.argv) < 1:
    print("{0} arguments.")
    exit(1)
else:
    print("{:d} argument:".format(len(sys.argv)))
    print("{}: {}".format(sys.argv[1], sys.argv))

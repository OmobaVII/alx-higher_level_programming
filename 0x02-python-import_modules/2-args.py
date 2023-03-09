#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    usrin = argv[1:]
    if len(argv) == 1:
        print("0 arguments.")
    elif len(argv) == 2:
        print("{:d} argument:".format(len(argv) - 1))
        for i, arg in enumerate(argv[1:]):
            print("{:d}: {}".format(i + 1, arg))
    else:
        print("{:d} arguments:".format(len(argv) - 1))
        for i, arg in enumerate(argv[1:]):
            print("{:d}: {}".format(i + 1, arg))

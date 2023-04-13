#!/usr/bin/python3
"""
this is the 101-stats module
this module is a script
"""


import sys
"""important for the stdin"""

from collections import defaultdict
"""for the dict"""

def print_the_stats(size, stat_codes):
    print(f"File size: {size}")
    for key in sorted(stat_codes):
        print(f"{key}: {stat_codes[key]}")

if __name__ == "__main__":
    

    size = 0
    stat_codes = dict()
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    line_count = 0

    try:
        for line in sys.stdin:
            if line_count == 0:
                print_the_stats(size, stat_codes)
                line_count = 1
            else:
                line_count += 1

            line = line.split()

            try:
                if line[-2] in valid_codes:
                    if stat_codes.get(line[-2], -1) == -1:
                        stat_codes[line[-2]] = 1
                    else:
                        stat_codes[line[-2]] += 1
            except IndexError:
                pass
        print_the_stats(size, stat_codes)

    except KeyboardInterrupt:
        print_the_stats(size, stat_codes)


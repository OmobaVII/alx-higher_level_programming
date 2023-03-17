#!/usr/bin/python3
def roman_to_int(roman_string):
    dictionary = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    rom = 0
    a = 0
    for character in roman_string:
        value = dictionary[character]
        if a < value:
            rom = rom + value - 2 * a
        else:
            rom = rom + value
        a = value
    return (rom)

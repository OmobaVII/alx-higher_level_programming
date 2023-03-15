#!/usr/bin/python3
def weight_average(my_list=[]):
    numerator = 0
    denominator = 0
    if my_list == []:
        return (0)
    else:
        for x, y in my_list:
            numerator = numerator + (x * y)
            denominator = denominator + y
        return (numerator / denominator)

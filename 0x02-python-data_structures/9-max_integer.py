#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        maxint = sorted(my_list)[-1]
        return maxint
    return None

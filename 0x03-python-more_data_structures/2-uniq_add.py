#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_int = set()
    for element in my_list:
        if isinstance(element, int) and element not in uniq_int:
            uniq_int.add(element)
    return sum(uniq_int)

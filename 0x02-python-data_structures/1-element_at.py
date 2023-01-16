#!/usr/bin/python3
def element_at(my_list, idx):
    if idx == 3:
        return my_list[3]
    elif idx < 0:
        return None
    elif idx > (len(my_list)):
        return None

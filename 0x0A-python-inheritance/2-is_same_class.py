#!/usr/bin/python3
"""Function is_same_class will return True
if the object is exactly an instance of the
specified class ; otherwise False"""


def is_same_class(obj, a_class):
    """Tests if the object is an
    instance of the specified class"""
    if isinstance(obj, a_class):
        return True
    else:
        return False

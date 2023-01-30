#!/usr/bin/python3
"""inherits_from will return True
    if the object is an instance of
    a class that inherited (directly or
    indirectly) from the specified class;
    otherwise False"""


def inherits_from(obj, a_class):
    """Checks if obj is instance of
    class or inherited from a_class"""
    if type(obj) is a_class or not isinstance(obj, a_class):
        return False
    else:
        return True

#/usr/bin/python3
"""is_kind_of_class is a function that
    returns True if the object is an instance of,
    or if the object is an instance of a class
    that inherited from, the specified class ;
    otherwise False"""


def is_kind_of_class(obj, a_class):
    """Checks if obj is an instance of,
    or is inherited from a_class """
    if isinstance(obj, a_class):
        return True
    else:
        return False

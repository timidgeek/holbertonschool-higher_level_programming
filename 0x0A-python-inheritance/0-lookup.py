#!/usr/bin/python3
"""
This is the lookup module, which returns
the list of available attributes and methods
of an object.
"""


def lookup(obj):
    """Simple function that returns all
    attributes and methods of list 'obj'"""
    return dir(obj)

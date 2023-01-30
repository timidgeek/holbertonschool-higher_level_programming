#!/usr/bin/python3
"""Declaring class BaseGeometry,
    with public instance area"""


class BaseGeometry:
    """Creating public instance method"""
    def area(self):
        raise Exception("area() is not implemented")

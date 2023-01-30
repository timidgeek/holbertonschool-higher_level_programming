#!/usr/bin/python3
"""Declaring class BaseGeometry,
    with public instances area
    and integer_validator"""


class BaseGeometry:
    """Creating public instance method"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError(name +" must be an integer")
        if value <= 0:
            raise ValueError(name +" must be greater than 0")

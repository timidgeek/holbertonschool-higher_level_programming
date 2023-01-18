#!/usr/bin/python3
"""Defines a class Square given parameters"""


class Square:
    """Declare the square"""
    def __init__(self, size=0):
        """Initialize new square"""
        if not isinstance(size, int):
                raise TypeError("size must be an integer")
        elif size < 0:
                raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return area of the square"""
        return (self.__size * self.__size)

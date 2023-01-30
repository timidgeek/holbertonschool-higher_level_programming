#!/usr/bin/python3
"""New class Square that inherits from
    Rectangle of ``9-rectangle.py``"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Inherits from Rectangle, initializes size"""
    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """Calculates area of rectangle"""
        return self.__size * self.__size

    def __str__(self):
        """Will print rectangle dimmensions and squarea"""
        return "[Square] {}/{}".format(self.__size, self.__size)

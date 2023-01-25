#!/usr/bin/python3
# 3-rectangle.py
# Lindsey Thomas @timidgeek
"""Rectangle class, which defines a rectangle"""


class Rectangle:
    """Represent a rectangle"""

    def __init__(self, width=0, height=0):

        self.width = width
        self.height = height

    @property
    def width(self):
        """To retrieve width"""
        return self.__width

    @width.setter
    def width(self, value):
        """To set width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """To retrieve height"""
        return self.height

    @height.setter
    def height(self, value):
        """To set height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

        def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width * 2 + self.height * 2)

    def __str__(self):
        string = ""
        if self.__width == 0 or self.__height == 0:
            return string

        for i in range(self.__height):
            for j in range(self.__width):
                string += "#"
            if i < self.__height - 1:
                string += "\n"
        return string

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)

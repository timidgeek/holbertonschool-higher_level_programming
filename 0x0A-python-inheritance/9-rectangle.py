#!/usr/bin/python3
"""New class Rectangle that inherits from
    BaseGeometry of ``7-base_geometry.py``"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Inherits from BaseGeometry, initializes
        width and height"""
    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
        
    def area(self):
        """Calculates area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Will print rectangle dimmensions"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

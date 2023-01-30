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

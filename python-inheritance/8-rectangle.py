#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
Module - Rectangle
"""


class Rectangle(BaseGeometry):
    """
    Child class of BaseGeometry
    """
    def __init__(self, width, height):
        """
        - Initialise attributes width and height
        - Check if they're type int by using integers_validator()
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

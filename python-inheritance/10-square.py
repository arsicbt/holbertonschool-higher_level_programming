#!/usr/bin/python3
"""
Module Square - Create square that inherits from rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square (Rectangle):
    """
    Create a square base on rectangle class
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return super().area()

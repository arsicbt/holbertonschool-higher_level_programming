#!/usr/bin/python3
"""
Module - Base for geometry
"""


class BaseGeometry:
    """
    Raise an exeption cause area is not implemented
    """
    def area(self):
        raise Exception('area() is not implemented')

#!/usr/bin/python3
"""
Module - Base for geometry
"""


class BaseGeometry:
    """
    Handle some errors
    """
    def area(self):
        """
        Raise an execption if the area() is not implemented
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        Raise exeptions :  
        - if value is not int
        - if value is less than or aqual to 0
        """
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))

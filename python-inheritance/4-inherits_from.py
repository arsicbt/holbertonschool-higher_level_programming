#!/usr/bin/python3
"""
Module 4 that defines a function to check if an object
is an instance of a specified class
"""


def inherits_from(obj, a_class):
    """
    Check if object is in instance of class and not a class
    """
    return is isinstance(obj, a_class) and type(obj) is not a_class

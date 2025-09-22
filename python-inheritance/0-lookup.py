#!/usr/bin/python3
"""
Module 0-lookup
This module give an function that display
a list of available attributes and methods of an object.
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        list: A list of attribute and method names available for the object.
    """
    return dir(obj)

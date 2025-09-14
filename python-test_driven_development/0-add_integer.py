#!/usr/bin/python3
"""Math helper: adds 2 numbers, safe and simple."""


def add_integer(a, b=98):
    """Add 2 integers (or floats that get cast into integers).

    Args:
        a: the first number (int or float)
        b: the second number (int or float), 98 by default

    Returns:
        int: the sum of a and b, caste to floats

    Raises:
        TypeError: if a or b are not int/float
    """
    if type(a) is bool or not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if type(b) is bool or not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)

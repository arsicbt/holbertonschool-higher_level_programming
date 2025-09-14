#!/usr/bin/python3
"""
Module that contains the print_square function.
"""


def print_square(size):
    """
    Prints a square with the character #.

    Args:
        size: The size length of the square (must be an integer)

    Raises:
        TypeError: If size is not an integer
        ValueError: If size is less than 0
    """
    # Check if size is a float and less than 0 first
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    # Check if size is not an integer
    if not isinstance(size, int) or isinstance(size, bool):
        raise TypeError("size must be an integer")

    # Check if size is less than 0
    if size < 0:
        raise ValueError("size must be >= 0")

    # Print the square
    for i in range(size):
        print("#" * size)

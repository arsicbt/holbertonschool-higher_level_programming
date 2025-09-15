#!/usr/bin/python3
"""2-square module

This module defines a class `Square` with a private instance attribute `size`,
including basic validation on initialization.
"""


class Square():
    """A class that defines a square by its size."""

    def __init__(self, size=0):
        """Initialize a new Square instance.

        Args:
            size (int): The size of the square (must be a non-negative int).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

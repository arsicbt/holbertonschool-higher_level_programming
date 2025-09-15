#!/usr/bin/python3
"""1-square module

This module defines a class `Square` with a private instance attribute `size`.
"""


class Square():
    """A class that defines a square by its size."""

    def __init__(self, size):
        """Initialize a new Square instance.

        Args:
            size: The size of the square (no type/value checks here).
        """
        self.__size = size

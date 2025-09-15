#!/usr/bin/python3
"""3-square module

This module defines a class Square with:
- a private instance attribute size
- validation during instantiation
- a public method to compute area
"""

class Square():
    """A class that defines a square by its size.

    Attributes:
        __size (int): The size of the square (private).

    Methods:
        __init__(self, size=0):
            Initializes a new square with optional size.
            Validates that size is a non-negative integer.

        area(self):
            Returns the area of the square (size * size).
    """

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

    def area(self):
        """Compute and return the area of the square.

        Returns:
            int: The area of the square (size squared).
        """
        return self.__size * self.__size

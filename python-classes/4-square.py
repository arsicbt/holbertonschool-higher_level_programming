#!/usr/bin/python3
"""Module 4-square

This module defines a class Square with:
- a private instance attribute size
- getter and setter for size with validation
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
            size (int, optional): The size of the square (default 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.__size = size

    @property
    def size(self):
        """Retrieve the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Compute and return the area of the square.

        Returns:
            int: The area of the square (size squared).
        """
        return self.__size * self.__size

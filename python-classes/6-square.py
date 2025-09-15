#!/usr/bin/python3
"""Module 6-square

This module defines a class Square with:
- a private instance attribute size
- a private instance attribute position
- getter and setter for size with validation
- getter and setter for position with validation
- a public method to compute area
- a public method to print the square
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

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square instance.

        Args:
            size (int, optional): The size of the square (default 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @property
    def position(self):
        """Retrieve the position of the square.

        Returns:
            tuple: The position (x, y) of the square.
        """
        return self.__position

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

    @position.setter
    def position(self, value):
        """Set the position of the square with validation.

        Args:
            value (tuple): The position (x, y) of the square.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Compute and return the area of the square.

        Returns:
            int: The area of the square (size squared).
        """
        return self.__size * self.__size

    def my_print(self):
        """Print the square using the `#` character.
        If the size of the square is 0, prints an empty line.
        Otherwise, prints a square of dimensions size x size using `#`
        at the position specified by __position.

        The position[1] represents vertical offset (empty lines).
        The position[0] represents horizontal offset (spaces before each line).

        Example:
            For a square of size 3 at position (2, 1):

            (empty line for vertical offset)
              ###
              ###
              ###
        """
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            spaces = " " * self.__position[0]
            square_chars = "#" * self.__size
            print(spaces + square_chars)

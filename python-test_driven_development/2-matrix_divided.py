#!/usr/bin/python3
"""Module that contains the matrix_divided function."""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a given number.

    Args:
        matrix: list of lists of ints/floats
        div: int or float

    Returns:
        new matrix with all elements divided by div, rounded to 2 decimals

    Raises:
        TypeError: if matrix is not a list of lists of ints/floats
        TypeError: if rows of matrix don't have the same size
        TypeError: if div is not a number
        ZeroDivisionError: if div is zero
    """
    if not isinstance(matrix, list) or not matrix:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    row_length = len(matrix[0])

    for row in matrix:
        if not isinstance(row, list) or not row:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
            )
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of int/floats"
                )

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Build new matrix using list comprehension, rounding each element
    return [[round(elem / div, 2) for elem in row] for row in matrix]

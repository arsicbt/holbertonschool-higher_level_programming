#!/usr/bin/python3
"""Helper to divide all numbers in a matrix safely!"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by div and return a new matrix.

    Args:
        matrix (list of lists of int/float): the matrix to divide
        div (int/float): the divisor

    Returns:
        list: new matrix with all elements divided by div, rounded to 2 dec

    Raises:
        TypeError: if matrix is not a list of lists of numbers
        TypeError: if rows are not all the same size
        TypeError: if div is not a number
        ZeroDivisionError: if div is 0
    """
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    row_size = len(matrix[0])
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
            )
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of int/floats"
                )

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_matrix.append([round(element / div, 2) for element in row])

    return new_matrix

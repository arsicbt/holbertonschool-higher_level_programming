#!/usr/bin/python3
"""
Module that contains the matrix_divided function.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Args:
        matrix: A list of lists of integers or floats
        div: A number (integer or float) to divide by

    Returns:
        A new matrix with all elements divided by div, rounded to 2 decimal
        places

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats
        TypeError: If rows of matrix don't have the same size
        TypeError: If div is not a number
        ZeroDivisionError: If div is equal to 0
    """
    # Check if matrix is a list of lists of integers/floats
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    # Check if all elements in matrix are lists and contain only numbers
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of "
                            "integers/floats")

        # Check for empty rows
        if len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) of "
                            "integers/floats")

        # Check if all elements in each row are integers or floats
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of "
                                "integers/floats")

    # Check if all rows have the same size
    if len(matrix) > 0:
        row_size = len(matrix[0])
        for row in matrix:
            if len(row) != row_size:
                raise TypeError("Each row must have the same size")

    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is not zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Create new matrix with divided elements rounded to 2 decimal places
    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            new_row.append(round(element / div, 2))
        new_matrix.append(new_row)

    return new_matrix

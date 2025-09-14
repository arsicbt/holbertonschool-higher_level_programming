#!/usr/bin/python3
"""A motivated helper to divide all numbers in a matrix safely!"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by div and return a new matrix.

    Args:
        matrix (list of lists of int/float): the matrix to divide
        div (int/float): the divisor

    Returns:
        list: new matrix with all elements divided by div, rounded to 2 decimals

    Raises:
        TypeError: if matrix is not a list of lists of numbers
        TypeError: if rows are not all the same size
        TypeError: if div is not a number
        ZeroDivisionError: if div is 0
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if len(matrix) == 0 or any(len(row) == 0 for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        if not all(isinstance(x, (int, float)) for x in row):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Create new matrix with rounded division
    new_matrix = []
    for row in matrix:
        new_matrix.append([round(x / div, 2) for x in row])

    return new_matrix

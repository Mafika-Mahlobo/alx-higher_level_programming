#!/usr/bin/python3
"""
Module with single function that divides all integers in a matrix

matrix_divided(matrix, div)
"""


def matrix_divided(matrix, div):

    """
    function to divide all integers in a matrix

    Args:
        matrix(list[]): list of lists with integers
        div(int): integer to divide

    Returns: matrix (list of lists)
    """

    new_matrix = []

    for i in range(1, len(matrix)):
        if not len(matrix[i]) == len(matrix[i - 1]):
            raise TypeError("Each row of the matrix must have the same size")

    for lis in matrix:
        for number in lis:
            if not isinstance(number, (int, float)):
                raise TypeError("matrix must be a matrix"
                                " list of lists) of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for row in matrix:

        new_row = []

        for element in row:
            temp = round((element / div), 2)
            new_row.append(temp)

        new_matrix.append(new_row)

    return new_matrix

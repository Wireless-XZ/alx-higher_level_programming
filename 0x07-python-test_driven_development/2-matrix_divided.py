#!/usr/bin/python3
"""
The "2-matrix_dividend" module

The module has one function "matrix_dividend"
"""


def matrix_divided(matrix, div):
    """
    Returns matrix[i][j] / div
    """
    if type(matrix) is not list or type(matrix[0]) is not list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        for col in row:
            if type(col) is not int and type(col) is not float:
                raise TypeError(
                    "matrix must be a matrix \
(list of lists) of integers/floats")

    size = len(matrix[0])
    new_matrix = [[]]

    for row in matrix:
        if size != len(row):
            raise TypeError("Each row of the matrix must have the same size")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    x = 0
    for rows in matrix:
        for cols in rows:
            new_matrix[x].append(round(cols/div, 2))
        new_matrix.append([])
        x += 1

    new_matrix.pop()
    return new_matrix

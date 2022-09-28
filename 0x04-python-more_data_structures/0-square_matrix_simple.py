#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_ = []
    for row in matrix:
        matrix_.append([x**2 for x in row])
    return matrix_

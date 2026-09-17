#!/usr/bin/python3


"""
    This module creates a new matrix of the division of a matrix using the
    following methods:
    matrix_divided
"""


def matrix_divided(matrix, div):
    """
    Returns a new matrix with the result by dividing all elements of a matrix.
    """
    result = 0
    new_matrix = []
    err_msg = "matrix must be a matrix (list of lists) of integers/floats"
    matrix_len = len(matrix[0])
    for row in matrix:
        new_list = []
        if matrix_len is not len(row):
            raise TypeError('Each row of the matrix must have the same size')
        for elem in row:
            if type(elem) is not int and type(elem) is not float:
                raise TypeError(err_msg)
            if type(div) is not int and type(div) is not float:
                raise TypeError('div must be a number')
            if div == 0:
                raise ZeroDivisionError('division by zero')
            result = round(elem / div, 2)
            new_list.append(result)
        new_matrix.append(new_list)
    return new_matrix

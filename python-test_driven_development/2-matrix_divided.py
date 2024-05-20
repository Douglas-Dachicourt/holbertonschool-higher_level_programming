#!/usr/bin/python3
"""This module is expected to divide all elements off a matrix

Returns a new matrix

"""


def matrix_divided(matrix, div):

    """The fonction takes two Arguments and returns an new and updated matrix:

        matrix : it is a list of a list. Each element has to be int/float
        div : the number to use for dividing all the elements

    """

    new_matrix = []

    for row in matrix:
        sub_list = []
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for x in row:
            if type(x) is not int and type(x) is not float:
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")
            elif type(div) is not int and type(div) is not float:
                raise TypeError("div must be a number")
            elif div == 0:
                raise ZeroDivisionError("division by zero")
            else:
                result = x / div

            round_result = round(result, 2)

            sub_list.append(round_result)
        new_matrix.append(sub_list)

    return new_matrix

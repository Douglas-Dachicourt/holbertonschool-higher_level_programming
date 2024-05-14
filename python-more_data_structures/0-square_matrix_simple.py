#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    ref = matrix
    new_matrix = []

    def power(my_list):
        return [x ** 2 for x in my_list[i]]

    for i in range(0, len(ref)):
        new_list = power(ref)
        new_matrix.append(new_list)

    return new_matrix

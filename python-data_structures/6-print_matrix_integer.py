#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    print()
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            print("{:d}".format(matrix[i][j]), end=" "
                  if matrix[i][j] != matrix[i][len(matrix[i]) - 1] else "\n")

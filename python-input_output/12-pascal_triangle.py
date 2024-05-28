#!/usr/bin/python3
"""
Function: pascal_triangle that print out a pascal rectangle

Attributes:

- n: an integer to give the 'size' of the rectangle
"""


def pascal_triangle(n):

    a_list = []

    if n <= 0:
        print(a_list)
    else:
        a_list.append([1])

    for i in range(1, n):

        row = [1]

        for j in range(1, i):
            row.append(a_list[i-1][j-1] + a_list[i-1][j])

        row.append(1)

        a_list.append(row)

    return a_list

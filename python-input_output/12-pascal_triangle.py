#!/usr/bin/python3
"""
This module helps to print out a pascal rectangle


"""


def pascal_triangle(n):
    """
    Function pascal_triangle that prints out a full pascal rectangle for a
    given size

    Attributes:

    - n: must a strict positive integer to give the 'size' of the rectangle

    Return:

    The triangle

    """

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

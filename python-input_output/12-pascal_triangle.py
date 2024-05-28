#!/usr/bin/python3
"""
This module helps to print out a pascal rectangle for a given size.
For example and a given size of 5 , we shoud have that following
representation in stdout:
[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]

"""


def pascal_triangle(n):
    """
    Function :

    - pascal_triangle() that prints out a full pascal rectangle for a
    given size

    Attributes:

    - n: must a strict positive integer to give the 'size' of the rectangle

    Return:

    The triangle as a list of lists

    """

    a_list = []

    if n <= 0:
        return a_list
    else:
        a_list.append([1])

    for i in range(1, n):

        row = [1]

        for j in range(1, i):
            row.append(a_list[i-1][j-1] + a_list[i-1][j])

        row.append(1)

        a_list.append(row)

    return a_list

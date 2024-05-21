#!/usr/bin/python3
"""This module is giving a fonction to print a square of "#"

    function print_square(size)

    Arg: 1 => size. Must be an positive integer ONLY

    Example:
    >>> print_square(4)
    ####
    ####
    ####
    ####

"""


def print_square(size):
    """Main function to print the square

    Verifies a few conditions

    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    else:
        for i in range(size):
            for j in range(size):
                print("#", end="" if j != size - 1 else "\n")

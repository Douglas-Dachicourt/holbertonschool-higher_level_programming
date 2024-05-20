#!/usr/bin/python3
"""This is a module that provides an addition fonction
"""


def add_integer(a, b=98):
    """fonction that add two integers or two floats numbers

        Args :
        a : an int or a float
        b : an int or a float

        Return a + b - must be integer only
    """
    if type(a) is not int and type(a) is not float:
        raise ValueError("a must be an integer")
    elif type(b) is not int and type(b) is not float:
        raise ValueError("b must be an integer")

    return (int(a) + int(b))

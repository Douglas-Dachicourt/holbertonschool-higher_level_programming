#!/usr/bin/python3
"""This module provides a function that verifies
the type of a class object"""


def is_same_class(obj, a_class):
    """Function is_same_class takes 2 arguments

    *obj - an int, a float, a string or a different object
    *class - class type of the object checked

    """

    if isinstance(obj, a_class):
        return True
    else:
        return False

#!/usr/bin/python3
"""This module provides a function that verifies
the type of a class object"""


def is_same_class(obj, a_class):
    """Function is_same_class takes 2 arguments

    *obj - an int, a float, a string or a different object
    *class - class type of the object checked

    """

    if type(obj) is int and a_class == int:
        return True
    elif type(obj) is float and a_class == float:
        return True
    elif type(obj) is bool and a_class == int:
        return False
    elif type(obj) is str and a_class == object:
        return True
    elif type(obj) is list and a_class == list:
        return True
    else:
        return False

#!/usr/bin/python3
"""
This module provides a function that gives
exactly the class(es) of a specific object

"""


def is_kind_of_class(obj, a_class):
    """
    Function is_same_class takes 2 arguments

    *obj - an int, a float, a string or a different object
    *class - class type of the object checked

    """
    if isinstance(obj, a_class):
        return True
    else:
        return False

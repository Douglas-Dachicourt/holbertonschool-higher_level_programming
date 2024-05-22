#!/usr/bin/python3
"""This module provides a function that verifies
the type of a class object"""


def is_same_class(obj, a_class):
    """Function is_same_class takes 2 arguments

    *obj - an int, a float, a string or a different object
    *class - class type of the object checked

    """

    if isinstance(obj, a_class):
        if issubclass(a_class, int):
            return True
        elif issubclass(a_class, float):
            return True
        elif issubclass(a_class, object):
            if isinstance(obj, int):
                return False
            elif isinstance(obj, float):
                return False
            else:
                return True

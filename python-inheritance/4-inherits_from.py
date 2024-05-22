#!/usr/bin/python3
"""
This module provides a function that checks the direct
or inderect inheritance of an an object to a class

"""


def inherits_from(obj, a_class):
    """
    2 arguments:

    obj: the object to test
    a_class: the class to compare with the object

    Returns:
    True if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class
    OTHERWISE False

    """

    check = type(obj)

    if check == a_class:
        return False

    if issubclass(check, a_class):
        return True
    else:
        return False

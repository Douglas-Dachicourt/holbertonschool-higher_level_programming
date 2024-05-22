#!/usr/bin/python3
"""This module is giving a specific function to
list methods and attributes in relation with an object

"""


def lookup(obj):
    """function that returns a list of attributes
    and methods in an object

    Arguments:
    obj

    """
    list_obj = dir(obj)
    return list_obj

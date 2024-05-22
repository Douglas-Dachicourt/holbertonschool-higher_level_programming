#!/usr/bin/python3
def lookup(obj):
    """function that returns a list of attributes
    and methods in an object
    """
    list_obj = dir(obj)
    return list_obj

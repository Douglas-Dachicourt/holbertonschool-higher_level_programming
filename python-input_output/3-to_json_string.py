#!/usr/bin/python3

"""
import json module
"""
import json


def to_json_string(my_obj):
    """
    Function : to_json_string

    This function returns the JSON string representation
    of a Python data structure.


    Arguments :

    - my_obj: the Python data structure to convert to
    JSON string


    Return:

    The JSON string representation of the Python data structure

    """
    return json.dumps(my_obj)

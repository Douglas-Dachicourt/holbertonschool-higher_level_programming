#!/usr/bin/python3
import json

"""
This module is providing a function that returns an object
(Python data structure) represented by a JSON string

We have to import first the module JSON (import json)
"""


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

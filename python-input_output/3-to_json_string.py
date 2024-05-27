#!/usr/bin/python3
import json

"""
This module is providing a function that returns an object
(Python data structure) represented by a JSON string

We have to import first the module JSON
"""


def to_json_string(my_obj):
    """
    Function : to_json_string

    Arguments :

    - my_obj: the data from the json file we want to work with

    Return:

    The object represented by a JSON string

    """

    return json.dumps(my_obj)

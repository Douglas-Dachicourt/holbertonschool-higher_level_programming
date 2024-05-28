#!/usr/bin/python3
"""class_to_json is a function that returns the dictionary description
with simple data structure (list, dictionary, string, integer and boolean)
for JSON serialization of an object"""


def class_to_json(obj):
    """
    Function : class_to_json

    Arguments:

    - obj : obj to test

    Return :
    The dictionary description with keys and values


    """
    details = obj.__dict__
    return details

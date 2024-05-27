#!/usr/bin/python3
"""
import json module
"""
import json


def load_from_json_file(filename):
    """
    Function : load_from_json_file is creating an object from
    a json file

    Arguments:

    - filename: the file file to work with

    Return:

    the object created

    """

    with open(filename, "r", encoding="utf-8") as fic:
        r = json.load(fic)
        return r

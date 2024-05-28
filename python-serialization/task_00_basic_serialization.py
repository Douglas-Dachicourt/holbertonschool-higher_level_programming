#!/usr/bin/python3
"""
import json module
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Function:

    - serialize_and_save_to_file:
    => serialize and save data to the specified file

    Parameters:

    - data: A Python Dictionary with data

    - filename: The filename of the output JSON file.
    If the output file already exists it should be replaced.

    """
    with open(filename, "w", encoding="utf-8") as f:
        to_save = json.dump(data, f)
        return to_save


def load_and_deserialize(filename):
    """
    Function:

    - load_and_deserialize:
    => load and deserialize data from the specified file

    Parameter:

    - filename: The filename of the input JSON file.

    Return:

    =>returns a Python Dictionary with the deseialized JSON data from the file.


    """
    with open(filename, "r", encoding="utf-8") as f:
        to_load = json.load(f)
        return to_load

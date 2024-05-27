#!/usr/bin/python3
"""
import json module
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Function : save_to_json_file is saving an object in
    a json file

    Arguments:

    - my_obj: the object ton save on the file
    - filename: the file to modify

    Return:

    a json file file with the name of the oject saved

    """
    with open(filename, "w", encoding="utf-8") as fic:
        x = json.dump(my_obj, fic)
        return x

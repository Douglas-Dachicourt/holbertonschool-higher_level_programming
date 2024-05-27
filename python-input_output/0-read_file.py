#!/usr/bin/python3
"""
This module provides a function to open and read
a text file

"""


def read_file(filename=""):
    """
    Function read_file:

    1 argument:

    the way to the file we want to open and read


    """
    with open(filename, 'r', encoding="utf-8") as fic:
        content = fic.read()
        print(content)

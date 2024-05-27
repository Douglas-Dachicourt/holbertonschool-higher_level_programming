#!/usr/bin/python3
"""
This module provides a function to open and read
a text file. It implements a function called read_file,
taking one argument

"""


def read_file(filename=""):
    """
    Function read_file:

    This function open a text file specified by the arguement
    passed and prints out the text to stdout

    Arguments:

    filename : type str giving the way of the file we want to open
    and read


    """
    with open(filename, 'r', encoding="utf-8") as fic:
        content = fic.read()
        print(content)

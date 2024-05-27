#!/usr/bin/python3
"""
This module provides a function to open and read
a text file. It implements a function called read_file,
taking one argument

"""


def read_file(filename=""):
    """
    Function read_file:

    This function open a file(.txt) throught the argument
    passed and prints out the text in stdout

    1 argument:

    The way to the file we want to open and read


    """
    with open(filename, 'r', encoding="utf-8") as fic:
        content = fic.read()
        print(content)

#!/usr/bin/python3
"""
This module provides a function to overwrite a text file
with new content. It implements a function called write_file,
taking two arguments

"""


def write_file(filename="", text=""):
    """
    Function write_file:

    This function overwrites a text file with new content.
    This one use specified arguments and return the number
    of new characters printed out

    Arguments:

    - filename : type str giving the way of the file we want
    to overwrite

    - text: type str content to write

    Return:
    The number of new characters printed out.

    For example:
    text = "This School is so cool!"

    Function should return : 24 (integer)

    """
    with open(filename, "w", encoding="utf-8") as fic:
        for letter in text:
            letter = fic.write(text)
            return letter

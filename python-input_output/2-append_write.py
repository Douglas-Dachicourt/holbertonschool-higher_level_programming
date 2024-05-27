#!/usr/bin/python3
"""
This module provides a function to add new content
at the end of a text file.
It implements a function called append_write,
taking two arguments

"""


def append_write(filename="", text=""):
    """
    Function append_write:

    This function add new text at the end of text file
    already existing.
    This one use specified arguments and return the number
    of new characters printed out

    Arguments:

    - filename : type str giving the way of the file we want
    to add new content

    - text: type str content to add

    Return:
    The number of new characters printed out.

    For example:

    text = "This School is so cool!"
    text in the updated filename is :
    "This School is so cool!"
    "This School is so cool!"

    Function should return : 24 (integer)
    """

    with open(filename, "a", encoding="utf-8") as fic:
        for letter in text:
            letter = fic.write(text)
            return letter

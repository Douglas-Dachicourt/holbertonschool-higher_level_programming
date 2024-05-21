#!/usr/bin/python3
"""This module provides a function that prints two new lines
    when a specific caracter is found in a text

"""


def text_indentation(text):
    """
    function : text_indentation(text)
        Print two new lines when a specific caracter is found in a text

        One argument : text
            => MUST BE STRING ONLY

    The caracters to find are : ".", "?" and ":"

    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    i = 0

    while i < len(text):
        if text[i] in "?.:":
            print(text[i])
            print()
            i = i + 1
            while i > len(text) and text[i] == ' ':
                i = i + 1
        else:
            print(text[i], end="")

        i = i + 1

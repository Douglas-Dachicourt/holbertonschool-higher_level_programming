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

    else:
        for i in range(len(text)):
            if text[i] == ':' or text[i] == '?' or text[i] == '.':
                print("{}".format(text[i]), end="\n")
                #print("{}".format(text[i + 1]), end="\n")
            else:
                print("{}".format(text[i]), end="")
        print()

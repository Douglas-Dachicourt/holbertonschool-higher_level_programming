#!/usr/bin/python3
"""This module prints your first name and last name"""


def say_my_name(first_name, last_name=""):
    """
    2 arguments:

        first_name: must be string only
        last_name: must be string only
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")
    else:
        print(f"My name is {first_name} {last_name}")

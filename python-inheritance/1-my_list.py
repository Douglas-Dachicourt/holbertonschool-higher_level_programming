#!/usr/bin/python3
"""This module is creating a class that inherits anoter one

"""


class MyList(list):
    """class MyList that inherits the integrated python class 'list'

    """

    def __init__(self):
        """ Constructor of our class 'MyList'
        Using super() to retrieve all the properties of 'list'
        """
        super().__init__()

    def print_sorted(self):
        """ function to print a new sorted list
        """
        sorted_list = sorted(self)
        print(sorted_list)

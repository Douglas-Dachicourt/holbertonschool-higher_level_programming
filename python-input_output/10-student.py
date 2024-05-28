#!/usr/bin/python3
"""
Objective of this module is to define a student with a main class
which allows to print out informations of a student using
public method "to_json"

"""


class Student:
    """
    class Student : defines a student by his last name,
    name and age

    Methods:

    - to_json : retrieves a dictionary representation of a Student
    instance

    Return :

    A new dictionnary with values of last_name, name or age searched
    by the user


"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        else:
            new_dict = {}
            for attr in attrs:
                if hasattr(self, attr):
                    new_dict[attr] = getattr(self, attr)

            return new_dict

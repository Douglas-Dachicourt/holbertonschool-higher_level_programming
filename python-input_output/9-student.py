#!/usr/bin/python3
"""
import json module
"""
import json


class Student:
    """
    class Student : defines a student by his last name,
    name and age

    Methods:

    - to_json : retrieves a dictionary representation of a Student
    instance and returns it



"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__

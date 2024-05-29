#!/usr/bin/python3
"""
import pickle module
"""
import pickle
"""
This module's goal is to learn how to serialize and
deserialize custom Python objects using the pickle module.

We will use a main class called CustomObject and use
different methods


"""


class CustomObject:
    """
    class CustomOject:

    Attributes:

    - name: str type
    - age = int type
    - is_student = bool type

    Methods:

    - display :
    => method to print out the object’s attributes with the following
    format:
    Name: type string
    Age: type int
    Is_Student: type bool


    - serialize :
    =>  This method will take a filename as its parameter. Using the
    pickle module, it will serialize the current instance of the object
    and save it to the provided filename
    Return None if errors occured

    - deserialize : (classmethod)
    => This class method will take a filename as its parameter. Using
    the pickle module, it will load and return an instance of the CustomObject
    from the provided filename
    Return None if errors occured

    """

    def __init__(self, name: str, age: int, is_student: bool):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print("Name: {}".format(self.name), end="\n")
        print("Age: {}".format(self.age), end="\n")
        print("Is_Student: {}".format(self.is_student), end="\n")

    def serialize(self, filename):
        try:
            with open(filename, "wb") as f:
                data = pickle.dump(self, f)
                return data
        except (pickle.PickleError, TypeError, AttributeError):
            return None

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, "rb") as f:
                data = pickle.load(f)
                return data
        except (pickle.Unpickler, AttributeError, TypeError):
            return None

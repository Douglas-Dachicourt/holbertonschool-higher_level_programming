#!/usr/bin/python3
from abc import ABC, abstractmethod

"""Objectives of this module: Create an abstract class named Animal using
the ABC package. This class should have an abstract method called sound.
Create two subclasses of Animal: Dog and Cat. Implement the sound method
in each subclass to return the strings “Bark” and “Meow” respectively.
"""


class Animal(ABC):
    """ Abstract class Animal using the ABC module to create abstract
    methods.

    Method:

    - sound : An abstract method that must be implemented by any subclass.
    """

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """Class Dog that inherits from Animal and implements the sound method.

    Method:
    - sound: Overrides the abstract method from Animal to return "Bark".
    """

    def sound(self):
        return f"Bark"


class Cat(Animal):
    """Class Cat that inherits from Animal and implements the sound method.

     Method:
     - sound: Overrides the abstract method from Animal to return "Meow".
     """

    def sound(self):
        return f"Meow"

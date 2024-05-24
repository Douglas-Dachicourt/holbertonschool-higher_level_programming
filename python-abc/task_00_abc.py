#!/usr/bin/python3
from abc import ABC, abstractmethod

"""Objectives of this module: Create an abstract class named Animal using
the ABC package. This class should have an abstract method called sound.
Create two subclasses of Animal: Dog and Cat. Implement the sound method
in each subclass to return the strings “Bark” and “Meow” respectively.
"""


class Animal(ABC):
    """ class Animal that inherit the ABC fonctionalities to
    create abstract methods

    Method:

    - sound : an abstract class
    """

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """Class Dog that inherit Animal and overrides the abstract
    method from there

    Method:

    - sound : overrides the abstract method from animal to print
    out a message to make dog bark

    """

    def sound(self):
        return f"Bark"


class Cat(Animal):
    """Class Cat that inherit Animal and overrides the abstract
    method from there

    Method:

    - sound : overrides the abstract method from animal to print
    out a message to make cat meows

    """

    def sound(self):
        return f"Meow"

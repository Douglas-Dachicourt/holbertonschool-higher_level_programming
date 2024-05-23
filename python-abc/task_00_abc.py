#!/usr/bin/python3
from abc import ABC, abstractmethod
"""This module is sharing a base class using an abstract method
and two subclasses that inherit the base
"""


class Animal(ABC):
    """Main abstract Animal class
    """

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """Subclass Dog that inhrits Animal"""

    def sound(self):
        return f"Bark"


class Cat(Animal):
    """Subclass Cat that inhrits Animal"""

    def sound(self):
        return f"Meow"

#!/usr/bin/python3
"""Objective of this module: Construct a FlyingFish class that inherits
from both a Fish class and a Bird class. Within FlyingFish, override methods
from both parents. The goal is to comprehend multiple inheritance and how
Python determines method resolution order (MRO)
"""


class Fish:
    """Class Fish

    Methods :
    - swim : Prints a message indicating the fish is swimming.
    - habitat: Prints a message indicating the habitat of the fish.


    """

    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")


class Bird:

    """Class Bird

    Methods :

    - fly : Prints a message indicating the bird is flying.
    - habitat : Prints a message indicating the habitat of the bird.


    """

    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):

    """Child class FlyingFish

    Inherits methods from Fish and Bird and overrides them:

    - fly : Prints a message indicating the flying fish is soaring.
    - swim : Prints a message indicating the flying fish is swimming.
    - habitat : Prints a message indicating the habitat of the flying fish.


    """

    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")


# ***********************-TESTING-***************************

animal = FlyingFish()


animal.fly()
# The flying fish is soaring!

animal.swim()
# The flying fish is swimming!

animal.habitat()
# The flying fish lives both in water and the sky!


print(FlyingFish.mro())
# [<class '__main__.FlyingFish'>, <class '__main__.Fish'>,
# <class '__main__.Bird'>, <class 'object'>]

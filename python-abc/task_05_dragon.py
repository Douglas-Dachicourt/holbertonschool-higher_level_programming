#!/usr/bin/python3
"""Objective of this module: Design of two mixin classes, SwimMixin
and FlyMixin, each equipped with methods swim and fly respectively.

Next, construction of a class Dragon that inherits from both these mixins.
The aim is to show that a Dragon instance can both swim and fly.
"""


class SwimMixin:
    """
        Class SwimMixin - Mixin class

        Method:

        -swim: prints out message that inform a creature is swimming

    """

    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """
        Class FlyMixin - Mixin class

        Method:

        -fly: prints out message that inform a creature is flying

    """

    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
        Class Dragon. Inherit both previous mixins 'SwimMixin' and
        'FlyMixin'

        Method:

        - roar: prints out message that inform a creature is roaring

    """

    def roar(self):
        print("The dragon roars!")


# ****************-TESTING-********************

draco = Dragon()

draco.swim()
# The creature swims!

draco.fly()
# The creature flies!

draco.roar()
# The dragon roars!

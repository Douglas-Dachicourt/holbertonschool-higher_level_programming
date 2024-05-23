#!/usr/bin/python3
from abc import ABC, abstractmethod
from math import pi
"""This module
"""


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):

    def __init__(self, radius=0):
        self.radius = radius

    def area(self):

        area = pi * ((self.radius) ** 2)
        return area

    def perimeter(self):

        perimeter = 2 * pi * self.radius
        return perimeter


class Rectangle(Shape):

    def __init__(self, height=0, width=0):
        self.height = height
        self.width = width

    def area(self):

        area = self.height * self.width
        return area

    def perimeter(self):

        perimeter = (2 * self.height) + (2 * self.width)
        return perimeter


def shape_info(shape):
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))

#!/usr/bin/python3
from abc import ABC, abstractmethod
from math import pi
"""Objective of this module : Create an abstract class named Shape with
two abstract methods: area and perimeter.

Implement two concrete classes: Circle and Rectangle, both inheriting
from Shape. Each class should provide implementations for the area and
perimeter methods.

Write a standalone function named 'shape_info' that accepts an object of
type Shape (by duck typing) and prints its area and perimeter.

Test the shape_info function with instances of both Circle and Rectangle.
"""


class Shape(ABC):
    """ Abstract class Shape using the ABC module to create abstract
    methods.

    Methods:

    - area : An abstract method that must be implemented by any subclass.
    - perimeter : An abstract method that must be implemented by any subclass.

    """

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """Class Circle that inherits from Shape and implements the area
    and perimeter methods.

    Methods:

    - area: Overrides the abstract method from Shape to return the area
    of a circle.

    - perimeter: Overrides the abstract method from Shape to return the
    perimeter of a circle.
    """

    def __init__(self, radius):
        self.radius = radius

    def area(self):

        area = pi * ((self.radius) ** 2)
        return area

    def perimeter(self):

        perimeter = 2 * pi * (abs(self.radius))
        return perimeter


class Rectangle(Shape):
    """Class Rectangle that inherits from Shape and implements the area
    and perimeter methods.

    Methods:

    - area: Overrides the abstract method from Shape to return the area
    of a rectangle.

    - perimeter: Overrides the abstract method from Shape to return the
    perimeter of a rectangle.
    """

    def __init__(self, height=0, width=0):
        self.height = height
        self.width = width

    def area(self):

        area = self.height * self.width
        return area

    def perimeter(self):

        perimeter = (2 * self.height) + (2 * self.width)
        return perimeter


"""
Standalone function 'shape_info' to print out the area and
perimeter of a circle or a rectangle

"""


def shape_info(shape):

    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))


# *****************-TESTING-**************************

cercle = Circle(radius=10)
rectangle = Rectangle(width=5, height=8)

shape_info(cercle)
# Area: 314.1592653589793
# Perimeter: 62.83185307179586

shape_info(rectangle)
# Area: 40
# Perimeter: 26

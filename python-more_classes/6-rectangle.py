#!/usr/bin/python3
"""This module provides a class that defines a rectangle

"""


class Rectangle:
    """Class Rectangle that defines a rectangle

        Args: 2
        width = must be integer = initially set at 0
        height = must be integer = initially set at 0


    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieve the initial size of width"""
        return self._Rectangle__width

    @width.setter
    def width(self, value):
        """Set the size with a new value"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

        self._Rectangle__width = value

    @property
    def height(self):
        """Retrieve the initial size of height"""
        return self._Rectangle__height

    @height.setter
    def height(self, value):
        """Set the size with a new value"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")

        self._Rectangle__height = value

    def area(self):
        """function that returns the area of the rectangle"""
        area = self._Rectangle__height * self._Rectangle__width
        return area

    def perimeter(self):
        """function that returns the perimeter of the rectangle"""
        perimeter = (self._Rectangle__height * 2) + \
            (self._Rectangle__width * 2)
        if self._Rectangle__width == 0 or self._Rectangle__height == 0:
            perimeter = 0

        return perimeter

    def __str__(self):
        """function that prints a vizualiation of the rectangle with #"""
        result = ""

        if self._Rectangle__height == 0 or self._Rectangle__width == 0:
            result = ""
            return result.strip()

        for i in range(self._Rectangle__height):
            for j in range(self._Rectangle__width):
                result = result + "#"
            result = result + "\n"
        return result.strip()

    def __repr__(self):
        """function that gives a representation
        of the rectangle with string type
        """
        width = self._Rectangle__width
        height = self._Rectangle__height

        return f"Rectangle({width}, {height})"

    def __del__(self):
        """function that delete a variable or an object"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

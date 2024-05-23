#!/usr/bin/python3
"""
    This module provides a class named as BaseGeometry
    Another class that is called Rectangle, that inherits
    from BaseGeometry
"""


class BaseGeometry:
    """
        the main original class.
    """

    def area(self):
        """area with the exception message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        # self.name = name

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

        if type(value) is bool:
            raise TypeError(f"{name} must be an integer")

        # self.value = value


class Rectangle(BaseGeometry):
    """
    class Rectangle, inheritates from BaseGeometry
    """

    def __init__(self, width, height):

        self._Rectangle__width = width
        self._Rectangle__height = height

        super().integer_validator(self._Rectangle__width, self._Rectangle__height)

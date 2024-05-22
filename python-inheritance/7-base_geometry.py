#!/usr/bin/python3
"""
    This module provides a class name as BaseGeometry
"""


class BaseGeometry:
    """
        the main original class.
    """

    def area(self):
        """area with the exception message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        self.name = name

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

        self.value = value

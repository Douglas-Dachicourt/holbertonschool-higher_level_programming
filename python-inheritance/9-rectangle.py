#!/usr/bin/python3

"""
    This module provides a class named as BaseGeometry
    Another class that is called Rectangle, that inherits
    from BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    class Rectangle, inheritates from BaseGeometry
    """

    def __init__(self, width, height):
        self._Rectangle__width = width
        self._Rectangle__height = height

        super().integer_validator("width", width)
        super().integer_validator("height", height)

    def area(self):
        area = self._Rectangle__height * self._Rectangle__width
        return area

    def __str__(self):
        r = "[Rectangle]"
        return (f"{r} {self._Rectangle__width}/{self._Rectangle__height}")

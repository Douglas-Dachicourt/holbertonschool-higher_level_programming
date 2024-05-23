#!/usr/bin/python3
"""This module provides a class named as Square
    That class inherits from another class called
    Rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square, inherits from father's class Rectangle
    """

    def __init__(self, size):
        self._size = size

        super().integer_validator("size", size)
        super().integer_validator("size", size)

    def __str__(self):
        r = "[Square]"
        return (f"{r} {self._size}/{self._size}")

    def area(self):
        area = self._size * self._size
        return area

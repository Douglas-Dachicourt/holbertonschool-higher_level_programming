#!/usr/bin/python3
"""Class square creation
"""


class Square:
    """square class that defines a square"""
    def __init__(self, size=0):
        self._Square__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

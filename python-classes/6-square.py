#!/usr/bin/python3
"""Class square creation
"""


class Square:
    """square class that defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        self._Square__size = size
        self._Square__position = position
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return (self._Square__size * self._Square__size)

    @property
    def size(self):
        return self._Square__size

    @property
    def position(self):
        return self._Square__position

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

        self._Square__size = value

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(num, int) for num in value) or
            not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self._Square__position = value

    def my_print(self):
        size = self.size
        position = self.position

        if size == 0:
            print()
            return

        for _ in range(position[1]):
            print()

        for _ in range(size):
            print(" " * position[0] + "#" * size)

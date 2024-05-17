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

    def area(self):
        return (self._Square__size * self._Square__size)

    @property
    def size(self):
        return self._Square__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

        self._Square__size = value

    def my_print(self):
        size = self._Square__size
        if size == 0:
            print()
        else:
            for i in range(size):
                for j in range(size):
                    print("#", end="" if j != size - 1 else "\n")

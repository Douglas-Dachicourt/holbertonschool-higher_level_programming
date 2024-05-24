#!/usr/bin/python3
"""
"""


class CountedIterator:
    """

    """

    def __init__(self, iterator, count=0):

        self.iterator = iter(iterator)
        self.count = count

    def get_count(self):
        return self.count

    def __next__(self):

        item = next(self.iterator)

        if item:
            self.count = self.count + 1
            return item
        else:
            raise StopIteration

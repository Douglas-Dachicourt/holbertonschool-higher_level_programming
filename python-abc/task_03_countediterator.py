#!/usr/bin/python3
"""Objective of this module : Create a class named CountedIterator
that extends the built-in iterator obtained from the iter function.

The CountedIterator should keep track of the number of items that
have been iterated over. Specifically, you will need to override the
__next__ method to increment a counter each time an item is fetched.
"""


class CountedIterator:
    """
    CountedIterator class that extends a built-in iterator to keep track
    of the number of items iterated over.

    Attributes:

    - iterator: The internal iterator object.
    - count: The number of items that have been iterated over.

    Methods:

    - __init__(self, iterator, count=0): Initializes the CountedIterator
      with an iterator and an optional initial count.
    - get_count(self): Returns the current count of iterated items.
    - __next__(self): Returns the next item from the iterator and increments
      the count. Raises StopIteration if the iterator is exhausted.
    """

    def __init__(self, iterator, count=0):
        """
        Initializes the CountedIterator with an iterator and an optional
        initial count.

        Parameters:

        - iterator: An iterable to be converted into an iterator.
        - count: The initial count of iterated items (default is 0).
        """
        self.iterator = iter(iterator)
        self.count = count

    def get_count(self):
        """
        Returns the current count of iterated items.

        Returns:

        - int: The number of items that have been iterated over.

        """
        return self.count

    def __next__(self):
        """
        Returns the next item from the iterator and increments the count.

        Returns:

        - The next item from the iterator.

        Raises:

        - StopIteration: If the iterator is exhausted.
        """

        item = next(self.iterator)

        if item:
            self.count = self.count + 1
            return item
        else:
            raise StopIteration

# ********************-TESTING-***************************


data = [3, 30, 300]

counted_iter = CountedIterator(data)

try:
    while True:
        item = next(counted_iter)
        print(f"Got {item}, total {counted_iter.get_count()} items iterated.")

except StopIteration:
    print("No more items.")

# Got 3, total 1 items iterated.
# Got 30, total 2 items iterated.
# Got 300, total 3 items iterated.
# No more items.

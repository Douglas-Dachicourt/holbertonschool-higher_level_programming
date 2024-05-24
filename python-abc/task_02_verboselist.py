#!/usr/bin/python3
"""Objective of this module : Create a class named VerboseList that extends
the Python list class. This custom class should print a notification message
every time an item is added (using the append or extend methods) or removed
(using the remove or pop methods).
"""


class VerboseList(list):
    """class VerboseList that inherits from the built-in list class

    This class override the original python methods append, extend, remove and
    pop that modify the list


    Methods:

    - append: After adding an item to the list, it should print which item is
    added
    - extend: After extending the list, it should print how many items have
    been added
    - remove: Before removing the item from the list, it should print which
    item is removed
    - pop: Before popping the item from the list, it should print which item
    is removed/popped

    All these methods use the super() function to be able to retrieve all the
    original functionalities from the built-in list class
    """

    def append(self, object):
        super().append(object)

        print(f"Added [{object}] to the list.")

    def extend(self, iterable):
        super().extend(iterable)

        num_items = 0

        for item in iterable:
            num_items = num_items + 1

        print(f"Extended the list with [{num_items}] items.")

    def remove(self, value):
        super().remove(value)

        print(f"Removed [{value}] from the list.")

    def pop(self, index=-1):

        item = super().pop(index)

        print(f"Popped [{item}] from the list.")

        return item


# ********************-TESTING-****************************


vl = VerboseList([1, 2, 3])
print(vl)
# [1, 2, 3]


vl.append(4)
# Added [4] to the list.
print(vl)
# [1, 2, 3, 4]

vl.extend([5, 6, 8, 9])
# Extended the list with [4] items.
print(vl)
# [1, 2, 3, 4, 5, 6, 8, 9]

vl.remove(2)
# Removed [2] from the list.
print(vl)
# 1, 3, 4, 5, 6, 8, 9]

vl.pop(3)
# Popped [5] from the list.
print(vl)
# [1, 3, 4, 6, 8, 9]

vl.pop()
# Popped [9] from the list.
print(vl)
# [1, 3, 4, 6, 8]

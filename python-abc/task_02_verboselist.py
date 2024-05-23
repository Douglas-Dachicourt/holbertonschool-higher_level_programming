#!/usr/bin/python3
"""
"""


class VerboseList(list):
    """
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


vl = VerboseList([1, 2, 3])
print(vl)

vl.append(4)
print(vl)

vl.extend([5, 6, 8, 9])
print(vl)

vl.remove(2)
print(vl)

vl.pop(3)
print(vl)

vl.pop()
print(vl)

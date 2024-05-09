#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, add(a, b)), end="\n")
    print("{} - {} = {}".format(a, b, sub(a, b)), end="\n")
    print("{} * {} = {}".format(a, b, mul(a, b)), end="\n")
    print("{} / {} = {}".format(a, b, div(a, b)), end="\n")

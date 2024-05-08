#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord('a') <= ord(c) <= ord('z'):
            upper = ord(c) - 32
            print("{}".format(chr(upper)), end="")
        else:
            print("{}".format(c), end="")
    print()

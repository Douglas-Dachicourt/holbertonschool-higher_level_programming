#!/usr/bin/python3
def uppercase(str):
    upper_str = ""
    for c in str:
        if ord('a') <= ord(c) <= ord('z'):
            upper_str += chr(ord(c) - 32)
        else:
            upper_str += chr(ord(c))
    print("{}".format(upper_str), end="")
    print()

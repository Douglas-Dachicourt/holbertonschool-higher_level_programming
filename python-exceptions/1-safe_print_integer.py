#!/usr/bin/python3
def safe_print_integer(value):
    try:

        if type(value) is int:
            print("{:d}".format(value))
            return True
        else:
            return False

    except ValueError:
        print(f"{value} is not an integer")

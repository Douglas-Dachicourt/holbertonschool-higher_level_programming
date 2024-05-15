#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):

    number = 0

    try:
        for num in range(0, x):

            print(my_list[num], end="")
            number = x

    except IndexError:
        pass

    print()

    return number

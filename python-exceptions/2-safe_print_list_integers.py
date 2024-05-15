#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    number = 0

    try:
        for num in range(0, x):
            if type(my_list[num]) is int:
                print("{:d}".format(my_list[num]), end="")
                number = my_list[num]
    except ZeroDivisionError:
        pass

    print()

    return number

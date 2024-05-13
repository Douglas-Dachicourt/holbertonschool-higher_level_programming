#!/usr/bin/python3
def max_integer(my_list=[]):

    len_list = len(my_list)

    if my_list == []:
        return None

    my_list.sort()
    return my_list[len_list - 1]

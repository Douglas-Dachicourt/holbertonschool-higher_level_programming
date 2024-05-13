#!/usr/bin/python3
def print_list_integer(my_list=[]):
    len_list = len(my_list)
    i = 0
    while i < len_list:
        print(f"{my_list[i]}")
        i += 1

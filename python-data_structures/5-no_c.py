#!/usr/bin/python3
def no_c(my_string):
    len_str = len(my_string)
    new_str = ""
    for i in range(0, len_str):
        if my_string[i] != 'c' and my_string[i] != 'C':
            new_str = new_str + my_string[i]

    return new_str

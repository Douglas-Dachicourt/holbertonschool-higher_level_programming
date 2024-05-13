#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    len_my_list = len(my_list)
    if idx < 0 or idx not in range(0, len_my_list):
        return my_list
    else:
        new_list = my_list
        del new_list[idx]
        new_list.insert(idx, element)
        return new_list

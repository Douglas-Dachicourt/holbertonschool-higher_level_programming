#!/usr/bin/python3
def uniq_add(my_list=[]):
    count = 0
    uniq_elem = set(my_list)

    for i in uniq_elem:
        count += i

    return count

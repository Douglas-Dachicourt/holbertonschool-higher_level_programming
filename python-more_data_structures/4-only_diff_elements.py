#!/usr/bin/python3
def only_diff_elements(set_1, set_2):

    diff_1 = set_1 - set_2
    diff_2 = set_2 - set_1
    fusion = diff_1 | diff_2
    only_diff = list(fusion)

    return only_diff

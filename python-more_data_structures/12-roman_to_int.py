#!/usr/bin/python3
def roman_to_int(roman_string):
    dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 100}

    if roman_string is None or type(roman_string) is not str:
        return 0

    count = 0
    prev_value = 0

    for c in reversed(roman_string):

        value = dict.get(c, 0)

        if value < prev_value:
            count = count - value
        else:
            count = count + value

        prev_value = value

    return count

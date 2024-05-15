#!/usr/bin/python3
def roman_to_int(roman_string):
    dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 100}

    count = 0

    if roman_string is None or type(roman_string) is not str:
        return None

    for i in range(0, len(roman_string)):
        for key, value in dict.items():
            if roman_string[i] == key:
                count += value
    return count

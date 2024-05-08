#!/usr/bin/python3
def print_last_digit(number):
    last_digit = number % 10
    str_format = ""

    if number == 0:
        str_format += '0'

    if number > 0:
        str_format += chr(last_digit)

    elif number < 0:
        number = - number
        last_digit -= 10
        last_digit = abs(last_digit)
        str_format += chr(last_digit)

    print("{}".format(last_digit), end="")

    return last_digit

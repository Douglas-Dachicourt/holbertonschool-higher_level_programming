#!/usr/bin/python3
def multiple_returns(sentence):

    if sentence == "":
        tuple = (0, "None")
        return tuple

    else:
        for let in sentence:

            len_str = len(sentence)
            letter = let

            tuple = (len_str, letter)
            return tuple

#!/usr/bin/python3
def multiple_returns(sentence):
    for let in sentence:
        len_str = len(sentence)
        letter = let
        tuple = (len_str, letter)
        return tuple

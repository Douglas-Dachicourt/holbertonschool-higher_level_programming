#!/usr/bin/python3
def best_score(a_dictionary):
    score_max = max(a_dictionary.values())

    for key, value in a_dictionary.items():
        if value == score_max:
            return key

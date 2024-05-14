#!/usr/bin/python3
def best_score(a_dictionary):
    score_max = max(a_dictionary.values())

    if a_dictionary == {} or a_dictionary == "None":
        return None

    for key, value in a_dictionary.items():
        if value == score_max:
            return key

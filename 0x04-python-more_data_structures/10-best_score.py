#!/usr/bin/python3
def best_score(a_dictionary):
    temp = 0
    if a_dictionary is None:
        return None
    else:
        for k, v in a_dictionary.items():
            if v > temp:
                temp = v

        for key, value in a_dictionary.items():
            if value == temp:
                return key

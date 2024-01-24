#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    mx_v = 0
    mx_k = None
    for k, v in a_dictionary.items():
        if v > mx_v:
            mx_v = v
            mx_k = k
    return mx_k

#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    for i in sorted(a_dictionary.values(), reverse=True):
        for j, k in a_dictionary.items():
            if i == k:
                return j

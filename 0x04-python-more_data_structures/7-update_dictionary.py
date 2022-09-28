#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if key not in a_dictionary.keys():
        a_dictionary[key] = value
    for i in a_dictionary.keys():
        if i is key:
            a_dictionary[i] = value
    return a_dictionary

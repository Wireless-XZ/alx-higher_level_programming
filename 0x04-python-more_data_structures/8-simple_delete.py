#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    for i in a_dictionary.keys():
        if i is key:
            del a_dictionary[i]
            break
    return a_dictionary

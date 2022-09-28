#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = my_list.copy()
    for j in new:
        if j == search:
            new[j - 1] = replace
    return new

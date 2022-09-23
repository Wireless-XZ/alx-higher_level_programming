#!/usr/bin/python3
def element_at(my_list, idx):
    x = 0
    if idx < 0 or idx > len(my_list):
        return None
    for i in my_list:
        if x == idx:
            return i
        x += 1

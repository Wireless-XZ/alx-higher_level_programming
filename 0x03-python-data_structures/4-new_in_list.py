#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        x = 0
        my_list_cpy = my_list.copy()
        for i in my_list:
            if x == idx:
                my_list_cpy[idx] = element
                return my_list_cpy
            x += 1

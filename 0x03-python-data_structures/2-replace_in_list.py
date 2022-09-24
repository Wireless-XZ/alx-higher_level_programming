#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        x = 0
        for i in my_list:
            if x == idx:
                my_list[idx] = element
                return my_list
            x += 1

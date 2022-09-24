#!/usr/bin/python3
def no_c(my_string):
    str_ = ""
    for i in my_string:
        if i != "c" and i != "C":
            str_ += i
    return str_

#!/usr/bin/python3
""" The '1-my_list' module
"""


class MyList(list):
    def print_sorted(self):
        print(sorted(self))

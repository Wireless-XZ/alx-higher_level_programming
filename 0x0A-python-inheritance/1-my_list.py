#!/usr/bin/python3
""" The '1-my_list' module
"""


class MyList(list):
    """ A class MyList that inherits from list
    """
    def __init__(self):
        """initializes the object
        """
        super().__init__()

    def print_sorted(self):
        """ prints the list, but sorted
        """
        print(sorted(self))

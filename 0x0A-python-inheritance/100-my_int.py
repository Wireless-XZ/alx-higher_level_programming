#!/usr/bin/python3
"""The "100-my_int" module
"""


class MyInt(int):
    """ Defines MyInt class
    """

    def __eq__(self, value):
        """Override == opeartor with != behavior"""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == behavior"""
        return self.real == value

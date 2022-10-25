#!/usr/bin/python3
"""The "0-lookup" module
"""


def lookup(obj):
    """Returns a list of all attributes in a class
    """
    return list(obj.__dict__.keys())

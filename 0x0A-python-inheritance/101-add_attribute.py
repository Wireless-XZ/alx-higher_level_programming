#!/usr/bin/python3
""" The "101-add_attribute" module
"""


def add_attribute(obj, key, value):
    """ adds an attribute to an object """
    if key not in (obj.__dict__).keys():
        (obj.__dict__)[key] = value
    else:
        raise TypeError("can't add new atrribute")

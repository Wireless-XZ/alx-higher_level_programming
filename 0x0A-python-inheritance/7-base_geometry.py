#!/usr/bin/python3
""" The '7-base_geometry' module
"""


class BaseGeometry:
    """ Class definition
    """
    def area(self):
        """ raises an Exception exception
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """ validates an integer
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

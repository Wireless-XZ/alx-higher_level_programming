#!/usr/bin/python3
""" The '8-rectangle' module
"""


class BaseGeometry:
    """ Class definition
    """
    def area(self):
        """ raises an Exception
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """ validates an integer
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """ Rectangle object
    """
    def __init__(self, width, height):
        """ Instantiate the Rectangle
        """
        self.integer_validator(width, width)
        self.__width = width
        self.integer_validator(height, height)
        self.__height = height

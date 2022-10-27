#!/usr/bin/python3
""" The '9-rectangle' module
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle object
    """
    def __init__(self, width, height):
        """ Instantiate the Rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """returns the area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """ prints a user friendly string
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

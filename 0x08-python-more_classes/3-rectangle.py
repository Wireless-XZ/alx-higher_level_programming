#!/usr/bin/python3
"""The "3-rectangle" module"""


class Rectangle:
    """A Rectangle object"""
    def __init__(self, width=0, height=0):
        """Initializes a Rectangle object"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """getter for the private instance attributr width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for the private instance attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for the private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for the private instance attribute"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns area of a rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """returns perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """prints a user friendly string"""
        list_ = []
        i = 0
        if self.__width != 0 and self.__height != 0:
            while i < self.__height:
                j = 0
                while j < self.__width:
                    list_.append('#')
                    j += 1
                list_.append('\n')
                i += 1

        list_.pop()
        return "".join(list_)
#!/usr/bin/python3
"""The "8-rectangle" module"""


class Rectangle:
    """A Rectangle object"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle object"""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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
        if self.__width != 0 and self.__height != 0:
            return '\n'.join([str(self.print_symbol) * self.__width
                              for i in range(self.__height)])
        return ""

    def __repr__(self):
        """prints class friendly string"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """prints a string when an object us deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) is not Rectangle:
            TypeError("rect_1 must be an instance of Rectangle")
        elif type(rect_2) is not Rectangle:
            TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() > rect_2.area():
            return rect_1
        if rect_1.area() == rect_2.area():
            return rect_1
        else:
            return rect_2

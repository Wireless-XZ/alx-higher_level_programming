#!/usr/bin/python3
"""Defines a Square class"""


class Square:
    """A Square object

    Attributes:
        __size (int): size of the square
    """
    def __init__(self, size=0):
        """Initializes the Square object

        Args:
            size (int): size of the square

        Returns: None
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size

    def area(self):
        """Computes the area of a square

        Returns: Area of a square
        """
        return self.__size ** 2

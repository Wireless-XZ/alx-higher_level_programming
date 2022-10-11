#!/usr/bin/python3
"""Defines a Square class"""


class Square:
    """A Square object

    Attributes:
        __size (int): size of the square
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initializes the Square object

        Args:
            size (int): size of the square
            position (int): square coordinates

        Returns: None
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        self.__position = position

    def area(self):
        """Computes the area of a square

        Returns: Area of a square
        """
        return self.__size ** 2

    @property
    def size(self):
        """Gets the size attribute

        Returns: __size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size attribute

        Returns: None
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    @property
    def position(self):
        """Gets the position attribute

        Returns: __position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position attribute

        Args:
            value (tuple): square coordinates

        Returns: None
        """
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or value[0] < 0 or \
           type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """prints the square

        Returns: None
        """
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for j in range(self.__size):
            print("".join([" " for k in range(self.__position[0])]), end="")
            print("".join(["#" for z in range(self.__size)]))

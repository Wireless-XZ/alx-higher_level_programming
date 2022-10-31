#!/usr/bin/python3
""" The `rectangle` module
"""


from models.base import Base


class Rectangle(Base):
    """ Rectangle class that inherited from Base class """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Args:
            width (int) = width
            height (int) = height
            x (int) = x
            y (int) = y
            id (int) = id
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ Getter for width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter for width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Getter for height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter for height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Getter for x """
        return self.__x

    @x.setter
    def x(self, value):
        """ Setter for x """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Getter for y """
        return self.__y

    @y.setter
    def y(self, value):
        """ Setter for y """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Returns the area of a rectangle """
        return self.height * self.width

    def display(self):
        """ prints to stdout the rectangle """
        for pad_y in range(0, self.y):
            print()
        for row in range(0, self.height):
            for pad_x in range(0, self.x):
                print(end=" ")
            for col in range(0, self.width):
                print("#", end="")
            print()

    def __str__(self):
        """ prints a user friendly string """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """ assigns argument to each attribute """
        attr_list = ['id', 'width', 'height', 'x', 'y']
        z = 0

        if args is not None and len(args) != 0:
            for i in range(z, len(args)):
                setattr(self, attr_list[z], args[z])
                z += 1
        elif kwargs is not None and len(kwargs) != 0:
            for key in kwargs:
                for i in attr_list:
                    if i == key:
                        setattr(self, key, kwargs[key])
                        break

    def to_dictionary(self):
        """ returns the dictionary representation of a Rectangle
        """
        attr_list = ['id', 'width', 'height', 'x', 'y']
        attr_dict = {}
        for att in attr_list:
            for key in self.__dict__:
                if key == 'id':
                    attr_dict[att] = (self.__dict__)[key]
                    break
                attr = '_Rectangle__' + att
                if key == attr:
                    attr_dict[att] = (self.__dict__)[key]
                    break
        return attr_dict

#!/usr/bin/python3
'''Module for Rectangle class.'''


from models.base import Base


class Rectangle(Base):
    """ rectangle class """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        """ x setter """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        """ y setter """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    def area(self):
        """ returns the area of the rectangle object """
        return self.width * self.height

    def display(self):
        """ displays a rectangle """
        rectangle = self.y * "\n"
        for i in range(self.height):
            rectangle += (" " * self.x)
            rectangle += ("#" * self.width) + "\n"

        print(rectangle, end='')

    def __str__(self):
        """ str """
        str = "[Rectangle] ({}) {}/{} - {}/{}"
        return str.format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs)
        """ update """
        attr = ['id', 'width', 'height', 'x', 'y']
        if args is not None and len(args) is not 0:
            i = 0
            for arg in args:
                setattr(self, attr[i], arg)
                i += 1
        else:
            for key, val in kwargs.items():
                setattr(self, key, val)
 

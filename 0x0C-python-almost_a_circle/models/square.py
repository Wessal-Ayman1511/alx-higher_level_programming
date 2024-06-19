#!/usr/bin/python3
'''Module for Square class.'''


from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class inhert from ractangle """
    def __init__(self, size, x=0, y=0, id=None):
        """ constructor """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ function """
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        """ width setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ update """
        attr = ['id', 'size', 'x', 'y']
        if args is not None and len(args) is not 0:
            i = 0
            for arg in args:
                setattr(self, attr[i], arg)
                i += 1
        else:
            for key, val in kwargs.items():
                setattr(self, key, val)

    def to_dictionary(self):
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}

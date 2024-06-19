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

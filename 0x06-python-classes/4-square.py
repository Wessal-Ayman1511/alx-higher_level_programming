#!/usr/bin/python3
"""Square Class"""


"""Square Class"""


class Square:
    """Square"""

    def __init__(self, size=0):
        """Constructor.
        Args:
            size: lenngth
        """
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Area of this square

        Return:
        the size
        """
        return self.__size ** 2

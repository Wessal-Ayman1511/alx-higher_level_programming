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
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """Area of this square

        Return:
        the size
        """
        return self.__size * self.__size

#!/usr/bin/python3
"""Square Class"""


"""Square Class"""


class Square:
    """Square"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        return self.position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(value, int) for num in value) or
            not all(num >= 2 for num in value)):
                raise TypeError("position must be a tuple of 2 positive integers")
        self.position = value

    def area(self):
        """Area of this square

        Return:
        the size
        """
        return self.__size ** 2

    def my_print(self):
        if self.size == 0:
            print("")
        else:
            [print("") for i in range(0, position[1])]
            for i in range(0, self.size):
                [print(" ", end='') for j in range(0, position[0])]
                [print("#", end='') for k in range(0, self.size)]
                print("")



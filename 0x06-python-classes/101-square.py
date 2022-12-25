#!/usr/bin/python3
"""class representing a square with a private instance attribute size."""


class Square:
    """Modelize a square."""
    def __str__(self):
        return (self.pos_print()[:-1])

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize the private instance attribute size.
        Args:
            size (int): the size of the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")

        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        if not all(isinstance(coord, int) for coord in value):
            raise TypeError("position must be a tuple of 2 positive integers")

        if not all(coord >= 0 for coord in value):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        return (self.__size * self.__size)

    def pos_print(self):
        pos = ""
        if not self.size:
            return "\n"

        for w in range(self.position[1]):
            pos += "\n"

        for w in range(self.size):
            for i in range(self.position[0]):
                pos += " "

            for j in range(self.size):
                pos += "#"

            pos += "\n"

        return (pos)

    def my_print(self):
        print(self.pos_print(), end='')

#!/usr/bin/python3
"""class representing a square with a private instance attribute size."""


class Square:
    """Modelize a square."""
    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize the private instance attribute size.
        Args:
            size (int): the size of the square.
        """
        self.__size = size
        self.__position = position

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

    def position(self, value):
        message = "position must be a tuple of 2 positive integers"
        if type(value) != tuple or value[0] < 0 or value[1] < 0:
            raise TypeError(message)

        self.__position = value

    def area(self):
        return (self.__size ** 2)

    def my_print(self):
        char = '#'
        if self.__size == 0:
            print()
            return

        [print("") for i in range(self.__position[1])]
        for i in range(self.__size):
            [print(" ", end="") for j in range(self.__position[0])]
            [print("{}".format(char), end="") for k in range(self.__size)]
            print()

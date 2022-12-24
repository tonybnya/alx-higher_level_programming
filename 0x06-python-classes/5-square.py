#!/usr/bin/python3
"""class representing a square with a private instance attribute size."""


class Square:
    """Modelize a square."""
    def __init__(self, size=0):
        """
        Initialize the private instance attribute size.
        Args:
            size (int): the size of the square.
        """
        self.size = size

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

    def area(self):
        return (self.__size ** 2)

    def my_print(self):
        char = '#'
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                [print("{}".format(char), end="") for j in range(self.__size)]
                print()

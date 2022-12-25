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
            raise TypeError("size must be a number")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        return (self.__size ** self.__size)

    def __eq__(self, new):
        return self.area() == new.area()

    def __ne__(self, new):
        return self.area() != new.area()

    def __lt__(self, new):
        return self.area() < new.area()

    def __le__(self, new):
        return self.area() <= new.area()

    def __gt__(self, new):
        return self.area() > new.area()

    def __ge__(self, new):
        return self.area() >= new.area()

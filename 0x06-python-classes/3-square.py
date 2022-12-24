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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        return (self._Square__size ** 2)

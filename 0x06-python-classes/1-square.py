#!/usr/bin/python3
"""class representing a square with a private instance attribute size."""


class Square:
    """Modelize a square."""
    def __init__(self, size):
        """
        Initialize the private instance attribute size.
        Args:
            size (int): the size of the square.
        """
        self.__size = size

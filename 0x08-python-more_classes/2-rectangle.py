#!/usr/bin/python3
"""
A module with a class that defines a rectangle.
This class has:
    - two private instance attributes width and height
    - a public instance method that returns the rectangle area
    - a public instance method that returns the rectangle perimeter
"""


class Rectangle:
    """Modelize a rectangle."""
    def __init__(self, width=0, height=0):
        """
        Initialize private instance attributes width and height.
        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Retrieve height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        return (self.__width + self.__height) * 2

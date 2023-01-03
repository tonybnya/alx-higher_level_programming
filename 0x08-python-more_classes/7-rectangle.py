#!/usr/bin/python3
"""
A module with a class that defines a rectangle.
This class has:
    - two private instance attributes width and height
    - a public instance method that returns the rectangle area
    - a public instance method that returns the rectangle perimeter
    - a public class attribute for number of instances
    - a public class attribute for a printing symbol
print() and str() should print the rectangle with the character #
repr() should return a string representation of the rectangle to be able
to recreate a new instance by using eval()
Print a message when an instance of Rectangle is deleted
"""


class Rectangle:
    """Modelize a rectangle."""

    # A class attribute representing the number of instances
    number_of_instances = 0
    # A class attibute used as symbol for string representation
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Initialize private instance attributes width and height.
        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

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
        if self.__width == 0 or self.__height == 0:
            return 0

        return (self.__width + self.__height) * 2

    def __str__(self):
        """
        Method to print the rectangle with the character #
        Returns:
            the string representation of the rectangle
        """
        rec = ""
        if self.__width == 0 or self.__height == 0:
            return rec

        for _ in range(self.__height):
            rec += (str(self.print_symbol) * self.__width) + '\n'

        return rec[:-1]

    def __repr__(self):
        """
        Method to return a string representation of a rectangle
        Using eval() can recreate a new instance of the object
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """
        Print a message when an instance is deleted
        """
        del self
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

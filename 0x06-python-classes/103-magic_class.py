"""Python class MagicClass for the given Python Bytecode."""
from math import pi


class MagicClass:
    """Define MagicClass."""
    def __init__(self, radius=0):
        """
        Initialize attributes.
        Arg:
            radius (float or int): the radius of the circle.
        """
        self.__radius = 0

        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")

        self.__radius = radius

    def area(self):
        """Area of the circle."""
        return (self.__radius ** 2 * pi)

    def circumference(self):
        """Circumference of the circle."""
        return (2 * pi * self.__radius)

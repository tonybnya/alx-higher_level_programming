#!/usr/bin/python3
"""
Class Rectangle that inherits from BaseGeometry based on 7-base_geometry.py
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class BaseGeometry(object):
    """
    Class BaseGeometry with an public instance method.
    """
    def area(self):
        """
        Public instance method not implemented yet.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Public instance method to validate 'value'
        'name'  is always a string.

        Args:
            name: name of the object
            value: value of the attribute
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    Python Inheritance
    Class Rectangle inherits from the base Class baseGeometry.
    """
    def __init__(self, width, height):
        """
        Initialize private attributes of the Class Rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.width = width
        self.height = height

#!/usr/bin/python3
"""
class Rectangle that inherits from Base class
This class has:
    - private instance attribute width
    - private instance attribute height
    - private instance attribute x
    - private instance attribute y
    - class constructor def __init__(self, width, height, x=0, y=0, id=None):
"""
from models.base import Base


class Rectangle(Base):
    """
    Python Inheritance.
    Class Rectangle inherits from Base Class.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialize private instance attributes. """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
#     @property
#     def width(self):
#         """ width getter """
#         return self.__width

#     @width.setter
#     def width(self, value):
#         """ width setter """
#         if type(value) is not int:
#             raise TypeError('width must be an integer')

#         if value <= 0:
#             raise ValueError('width must be > 0')

#         self.__width = value

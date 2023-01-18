#!/usr/bin/python3
"""
Class Square that inherits from Rectangle class.
This class has:
    - private instance attribute width
    - private instance attribute height
    - private instance attribute x
    - private instance attribute y
    - class constructor def __init__(self, size, x=0, y=0, id=None):
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Python Inheritance.
    Class Square inherits from Rectangle class.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """ Initialize instances from attributes of Rectangle class. """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Special method to print a custom string of a square object."""
        # [Square] (<id>) <x>/<y> - <size>
        string_start = "[Square] "
        string_id = "({}) ".format(self.id)
        string_xy = "{}/{} - ".format(self.x, self.y)
        string_s = "{}".format(self.width)

        return string_start + string_id + string_xy + string_s

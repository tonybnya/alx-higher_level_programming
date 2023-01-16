#!/usr/bin/python3
"""
First class Base as the base class for the entire project.
This class has:
    - a private class attribute __nb_objects
    - a class constructor def __init__(self, id=None):
"""


class Base:
    """ Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialize attributes """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

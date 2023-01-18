#!/usr/bin/python3
"""
Unit tests for Square class.
"""
import unittest
from unittest.mock import patch
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """ Test cases for Square class. """

    def setUp(self):
        """ Method called before each test. """
        Base._Base__nb_objects = 0

    def test_square_with_default_values(self):
        """ Test with default values. """
        square = Square(7)
        self.assertEqual(square.size, 7)
        self.assertEqual(square.width, 7)
        self.assertEqual(square.height, 7)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)
        self.assertEqual(square.id, 1)

    def test_square_with_custom_values(self):
        """ Test with custom values. """
        square = Square(5, 3, 3, 2)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
        self.assertEqual(square.x, 3)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.id, 2)

    def test_squares_comparison(self):
        """ Test to compare two squares. """
        square1 = Square(1, 1)
        square2 = Square(1, 1)
        self.assertEqual(False, square1 is square2)
        self.assertEqual(False, square1.id == square2.id)

    def test_is_Base_instance(self):
        """ Test Square is a Base instance. """
        square = Square(1)
        self.assertEqual(True, isinstance(square, Base))

    def test_is_Rectangle_instance(self):
        """ Test Square is a Rectangle instance. """
        square = Square(1)
        self.assertEqual(True, isinstance(square, Rectangle))

    def test_no_arguments(self):
        """ Test error raising with no argument passed. """
        with self.assertRaises(TypeError):
            square = Square()

    def test_number_of_arguments(self):
        """ Test error raised with no args passed """
        with self.assertRaises(TypeError):
            square = Square(1, 1, 1, 1, 1)

    def test_access_private_class_attribute_width(self):
        """ Test for trying to access to private attribute width. """
        square = Square(1)
        with self.assertRaises(AttributeError):
            square.__width

    def test_access_private_class_attribute_height(self):
        """ Test for trying to access to private attribute height. """
        square = Square(1)
        with self.assertRaises(AttributeError):
            square.__height

    def test_access_private_class_attribute_x(self):
        """ Test for trying to access to private attribute x. """
        square = Square(1)
        with self.assertRaises(AttributeError):
            square.__x

    def test_access_private_class_attribute_y(self):
        """ Test for trying to access to private attribute y. """
        square = Square(1)
        with self.assertRaises(AttributeError):
            square.__y

    def test_valid_attributes(self):
        """ Test for valid arg passing to the object. """
        with self.assertRaises(TypeError):
            square = Square("2", 2, 2, 2)

        with self.assertRaises(TypeError):
            square = Square(2, "2", 2, 2)

        with self.assertRaises(TypeError):
            square = Square(2, 2, "2", 2)

    def test_attributes_value(self):
        """ Test for attributes value. """
        with self.assertRaises(ValueError):
            square = Square(0)

        with self.assertRaises(ValueError):
            square = Square(1, -1)

        with self.assertRaises(ValueError):
            square = Square(1, 1, -1)

    def test_area0(self):
        """ Test for the return value of area method. """
        square = Square(4)
        self.assertEqual(square.area(), 16)

    def test_area1(self):
        """ Test for the return value of area method. """
        square = Square(2)
        self.assertEqual(square.area(), 4)
        square.size = 5
        self.assertEqual(square.area(), 25)

#!/usr/bin/python3
"""
Unit tests for Rectangle class.
"""
import unittest
from unittest.mock import patch
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """ Test cases for Rectangle class. """

    def setUp(self):
        """ Method called before each test. """
        Base._Base__nb_objects = 0

    def test_rectangle_with_default_values(self):
        """ Test instanciation with default values. """
        rec = Rectangle(3, 5)
        self.assertEqual(rec.width, 3)
        self.assertEqual(rec.height, 5)
        self.assertEqual(rec.x, 0)
        self.assertEqual(rec.y, 0)
        self.assertEqual(rec.id, 1)

    def test_rectangle_with_custom_values(self):
        """ Test instanciation with custom values. """
        rec = Rectangle(7, 9, 2, 3, 4)
        self.assertEqual(rec.width, 7)
        self.assertEqual(rec.height, 9)
        self.assertEqual(rec.x, 2)
        self.assertEqual(rec.y, 3)
        self.assertEqual(rec.id, 4)

    def test_rectangles_comparison(self):
        """ Test to compare two Rectangle objects. """
        rec1 = Rectangle(1, 1)
        rec2 = Rectangle(1, 1)
        self.assertEqual(False, rec1 is rec2)
        self.assertEqual(False, rec1.id == rec2.id)

    def test_is_Base_instance(self):
        """ Test for assert Rectangle object is an instance of Base. """
        rec = Rectangle(3, 4)
        self.assertEqual(True, isinstance(rec, Base))

    def test_one_argument(self):
        """ Test for one argument passing in the instanciation. """
        with self.assertRaises(TypeError):
            rec = Rectangle(9)

    def test_no_argument(self):
        """ Test for no argument passing in the instanciation. """
        with self.assertRaises(TypeError):
            rec = Rectangle()

    def test_accessing_to_private_class_attribute_width(self):
        """ Test access to private class attribute width. """
        rec = Rectangle(1, 2)
        with self.assertRaises(AttributeError):
            rec.__width

    def test_accessing_to_private_class_attribute_height(self):
        """ Test access to private class attribute height. """
        rec = Rectangle(1, 2)
        with self.assertRaises(AttributeError):
            rec.__height

    def test_accessing_to_private_class_attribute_x(self):
        """ Test access to private class attribute x. """
        rec = Rectangle(1, 2)
        with self.assertRaises(AttributeError):
            rec.__x

    def test_accessing_to_private_class_attribute_y(self):
        """ Test access to private class attribute y. """
        rec = Rectangle(1, 2)
        with self.assertRaises(AttributeError):
            rec.__y

    def test_area(self):
        """ Test for the return value of area method. """
        rec = Rectangle(4, 5)
        self.assertEqual(rec.area(), 20)

        rec.width = 3
        self.assertEqual(rec.area(), 15)

        rec.height = 9
        self.assertEqual(rec.area(), 27)

    def test_display(self):
        """ Test for Rectangle object printed using '#' character. """
        rec = Rectangle(4, 6)
        result = "####\n####\n####\n####\n####\n####\n"

        with patch('sys.stdout', new=StringIO()) as output:
            rec.display()
            self.assertEqual(output.getvalue(), result)

        rec.width = 3
        result = "###\n###\n###\n###\n###\n###\n"

        with patch('sys.stdout', new=StringIO()) as output:
            rec.display()
            self.assertEqual(output.getvalue(), result)

        rec.height = 5
        result = "###\n###\n###\n###\n###\n"

        with patch('sys.stdout', new=StringIO()) as output:
            rec.display()
            self.assertEqual(output.getvalue(), result)

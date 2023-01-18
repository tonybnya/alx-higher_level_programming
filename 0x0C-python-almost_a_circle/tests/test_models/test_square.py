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

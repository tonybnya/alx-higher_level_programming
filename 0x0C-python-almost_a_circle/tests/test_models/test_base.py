#!/usr/bin/python3
"""
Unit tests for Base class.
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """ Test cases for Base class. """

    def setUp(self):
        self.base = Base()

    def test_id_assignment(self):
        """ Test for id assignment. """
        self.assertEqual(self.base.id, 1)

    def test_id_assignment_with_custom_value(self):
        """ Test for id assignment with custom value. """
        base_2 = Base(10)
        self.assertEqual(base_2.id, 10)

    def test_class_attribute_nb_objects(self):
        """ Test for private class attribute __nb_objects. """
        self.assertEqual(Base.__nb_objects, 1)


if __name__ == '__main__':
    unittest.main()

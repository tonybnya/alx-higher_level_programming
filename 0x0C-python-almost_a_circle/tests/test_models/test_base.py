#!/usr/bin/python3
"""
Unit tests for Base class.
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """ Test cases for Base class. """

    def setUp(self):
        """ Method called before each test. """
        # self.base = Base()
        Base._Base__nb_objects = 0

    def test_id_assignment_with_custom_value(self):
        """ Test for id assignment with custom value. """
        base = Base(1)
        self.assertEqual(base.id, 1)

    def test_id_assignment_with_default_value(self):
        """ Test for id assignment with default value. """
        base = Base()
        self.assertEqual(base.id, 1)

    def test_private_class_attribute_nb_objects(self):
        """ Test for private class attribute __nb_objects. """
        base_1 = Base()
        base_2 = Base()
        base_3 = Base()
        self.assertEqual(base_1.id, 1)
        self.assertEqual(base_2.id, 2)
        self.assertEqual(base_3.id, 3)

    def test_private_class_attribute_nb_objects_mixed(self):
        """ Test for private class attribute __nb_objects and id assigment. """
        base_1 = Base()
        base_2 = Base(7)
        base_3 = Base()
        self.assertEqual(base_1.id, 1)
        self.assertEqual(base_2.id, 7)
        self.assertEqual(base_3.id, 2)

    def test_number_of_arguments(self):
        """ Test for number of arguments passing in the instanciation. """
        with self.assertRaises(TypeError):
            base = Base(1, 2)

    def test_accessing_to_private_class_attribute(self):
        """ Test access to private class attribute. """
        base = Base()
        with self.assertRaises(AttributeError):
            base.__nb_objects


if __name__ == '__main__':
    unittest.main()

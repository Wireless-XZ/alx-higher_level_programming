#!/usr/bin/python3
""" Unittest for base
"""
import unittest
from models.base import Base

class Test_Base(unittest.TestCase):
    """ unit test for Base class
    """
    def test_module_doc(self):
        """ Tests for module docstring """
        self.assertTrue(len(__import__("models").base.__doc__) > 1)

    def test_function_doc(self):
        """Tests for function docstring"""
        self.assertTrue(len(Base.__init__.__doc__) > 1)

    def test_class_doc(self):
        """Tests for class docstring"""
        self.assertTrue(len(Base.__doc__) > 1)

    def test_id_not_None(self):
        """ Tests for id is None """
        self.assertEqual(Base(12).id, 12)

    def test_id_None(self):
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base().id, 2)
        self.assertEqual(Base().id, 3)

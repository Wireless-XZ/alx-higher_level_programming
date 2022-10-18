#!/usr/bin/python3
"""Unittest for max_integer
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

def TestMaxInteger(unittest.TestCase):
    """unittest class for max_integer"""
    def test_module_doc(self):
        """Tests for module documentation"""
        x = __import__("6-max_integer").__doc__
        self.assertTrue(len(x) > 1)

    def test_function_doc(self):
        self.assertTrue(len(max_integer.__doc__) > 1)

    def test_positive_int_end(self):
        """Tests for max at end"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_positive_int_mid(self):
        """Tests for max in the middle"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_positive_int_begin(self):
        """Tests for max at the beginning"""
        self.assertEqual(max_integer([4, 3, 1, 2]), 4)

    def test_negative_int_end(self):
        """Tests for max -ve at the end"""
        self.assertEqual(max_integer([-4, -2, -3, -1]), -1)

    def test_negative_int_mid(self):
        """Tests for max -ve int in the middle"""
        self.asserEqual(max_integer([-3, -1, -4, -2]), -1)

    def test_negative_int_begin(self):
        """Tests for max -ve int at the beginning"""
        self.asserEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_empty_list(self):
        """Tests for empty list"""
        self.assertEqual(max_integer([]), None)

if __name__ == "__main__":
    unittest.main()

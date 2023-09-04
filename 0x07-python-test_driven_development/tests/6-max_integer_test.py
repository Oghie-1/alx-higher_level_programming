#!/usr/bin/python3
"""Unittest for the max_integer module
"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """TestCase for the max_integer function."""

    def test_empty_list(self):
        """Test with a regular list of ints: should return the max result"""
        result = max_integer([])
        self.assertIsNone(result, "Expected None for an empty list")

    def test_single_element_list(self):

        result = max_integer([42])
        self.assertEqual(result, 42, "Expected 42 for a single-element list")

    def test_positive_numbers(self):
        result = max_integer([1, 2, 3, 4, 5])
        self.assertEqual(result, 5, "Expected 5 as the maximum")

    def test_negative_numbers(self):
        """Test with a list of negative values: should return the max"""
        result = max_integer([-5, -3, -1, -2, -4])
        self.assertEqual(result, -1, "Expected -1 as the maximum")

    def test_mixed_numbers(self):
        result = max_integer([-5, 0, 5, -1, 2])
        self.assertEqual(result, 5, "Expected 5 as the maximum")

    def test_float_numbers(self):
        """Test with a list of mixed ints and floats: should return the max"""
        result = max_integer([1.5, 2.7, 3.2, 4.1])
        self.assertEqual(result, 4.1, "Expected 4.1 as the maximum")
    def test_unique(self):
        """Test with a list of one int: should return the value of this int"""
        l = [45]
        result = max_integer(l)
        self.assertEqual(result, 45)

    def test_identical(self):
        """Test with a list of identical values: should return the value"""
        l = [8, 8, 8, 8, 8]
        result = max_integer(l)
        self.assertEqual(result, 8)

    def test_strings(self):
        """Test with a list of strings: should return the first string"""
        l = ["hi", "hello"]
        result = max_integer(l)
        self.assertEqual(result, "hi")

    def test_none(self):
        """Test with a None as parameter: should raise a TypeError"""
        self.assertRaises(TypeError, max_integer, None)

if __name__ == '__main__':
    unittest.main()

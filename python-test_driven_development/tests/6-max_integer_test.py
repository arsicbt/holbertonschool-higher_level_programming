#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    def test_regular_list(self):
        """Test with a regular list of positive integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_single_element(self):
        """Test with a single element"""
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([0]), 0)
        self.assertEqual(max_integer([-5]), -5)

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertIsNone(max_integer([]))
        self.assertIsNone(max_integer())

    def test_negative_numbers(self):
        """Test with negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-5, -1, -3]), -1)
        self.assertEqual(max_integer([-10, -5, -2]), -2)

    def test_mixed_positive_negative(self):
        """Test with mixed positive and negative numbers"""
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)
        self.assertEqual(max_integer([5, -10, 3, -2]), 5)
        self.assertEqual(max_integer([-1, -2, 3]), 3)

    def test_duplicate_max(self):
        """Test with duplicate maximum values"""
        self.assertEqual(max_integer([4, 4, 4, 4]), 4)
        self.assertEqual(max_integer([1, 4, 2, 4, 3]), 4)
        self.assertEqual(max_integer([-1, -1, -1]), -1)

    def test_max_at_beginning(self):
        """Test when maximum is at the beginning"""
        self.assertEqual(max_integer([10, 1, 2, 3]), 10)
        self.assertEqual(max_integer([5, 4, 3, 2, 1]), 5)

    def test_max_at_end(self):
        """Test when maximum is at the end"""
        self.assertEqual(max_integer([1, 2, 3, 10]), 10)
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_max_in_middle(self):
        """Test when maximum is in the middle"""
        self.assertEqual(max_integer([1, 10, 2]), 10)
        self.assertEqual(max_integer([3, 1, 8, 2, 5]), 8)

    def test_zero_included(self):
        """Test with zero included in the list"""
        self.assertEqual(max_integer([0, 1, 2]), 2)
        self.assertEqual(max_integer([-1, 0, -2]), 0)
        self.assertEqual(max_integer([0, -1, -2]), 0)

    def test_large_numbers(self):
        """Test with large numbers"""
        self.assertEqual(max_integer([1000, 999, 1001]), 1001)
        self.assertEqual(max_integer([999999, 1000000, 999998]), 1000000)

    def test_float_numbers(self):
        """Test with float numbers"""
        self.assertEqual(max_integer([1.5, 2.7, 1.2]), 2.7)
        self.assertEqual(max_integer([3.14, 2.71, 1.41]), 3.14)
        self.assertEqual(max_integer([-1.5, -2.7, -1.2]), -1.2)

    def test_mixed_int_float(self):
        """Test with mixed integers and floats"""
        self.assertEqual(max_integer([1, 2.5, 3]), 3)
        self.assertEqual(max_integer([1.5, 2, 3.7, 2]), 3.7)

    def test_string_numbers(self):
        """Test with string representation of numbers"""
        # Note: This will compare strings lexicographically
        self.assertEqual(max_integer(['a', 'b', 'c']), 'c')
        self.assertEqual(max_integer(['z', 'a', 'm']), 'z')

    def test_very_long_list(self):
        """Test with a very long list"""
        long_list = list(range(1000))
        self.assertEqual(max_integer(long_list), 999)

        long_list_reverse = list(range(999, -1, -1))
        self.assertEqual(max_integer(long_list_reverse), 999)


if __name__ == '__main__':
    unittest.main()

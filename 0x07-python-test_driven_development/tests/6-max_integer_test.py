"""
This is a test file for max integer
"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class Max_integer_test(unittest.TestCase):

    """
    This class runs tests for the max_integer function in 6-max_integer module.
    two test functions with test cases.
    """

    def test_list_with_int(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([1, 10]), 10)
        self.assertEqual(max_integer([0]), 0)

    def test_zero_len(self):
        self.assertEqual(max_integer([]), None)

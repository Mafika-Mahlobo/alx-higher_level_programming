"""Test files for Base class"""
import unittest
from base import Base

class Base_test(unittest.TestCase):
    """Unittest class"""

    def test_without_id(self):
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base().id, 2)

    def test_with_id(self):
        self.assertEqual(Base(10).id, 10)

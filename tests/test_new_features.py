import unittest
from app import add, subtract

# Importing the tests from your custom_unittest module
# from cust_unittest import TestApp

# Define additional test cases or new tests here
class TestNewFeatures(unittest.TestCase):

    def test_add_negative_numbers(self):
        """Test addition with negative numbers."""
        self.assertEqual(add(-1, -1), -2)

    def test_subtract_negative_numbers(self):
        """Test subtraction with negative numbers."""
        self.assertEqual(subtract(-2, -1), -1)

    def test_add_large_numbers(self):
        """Test addition with large numbers."""
        self.assertEqual(add(1_000_000, 2_000_000), 3_000_000)

    def test_subtract_large_numbers(self):
        """Test subtraction with large numbers."""
        self.assertEqual(subtract(1_000_000, 500_000), 500_000)


if __name__ == '__main__':
    unittest.main()

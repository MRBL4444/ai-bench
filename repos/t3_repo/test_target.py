import unittest
from target import count_even

class TestCountEven(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(count_even([1,2,3,4]), 2)
    def test_empty(self):
        self.assertEqual(count_even([]), 0)
    def test_negative(self):
        self.assertEqual(count_even([-2,-3,-4]), 2)

if __name__ == "__main__":
    unittest.main()
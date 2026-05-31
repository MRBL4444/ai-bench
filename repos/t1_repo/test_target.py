import unittest
from target import add

class TestAddT1(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(add([1, 2, 3, 4]), 6)
        self.assertEqual(add([0, 1, 2, 3]), 2)
    def test_empty(self):
        self.assertEqual(add([]), 0)
    def test_negative(self):
        self.assertEqual(add([-2, -3, -4]), -6)

if __name__ == "__main__":
    unittest.main()
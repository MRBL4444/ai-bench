import unittest
from target import add

class TestAddT2(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(add([]), 0)
    def test_basic(self):
        self.assertEqual(add([1,2,3]), 6)
    def test_negative(self):
        self.assertEqual(add([-1,-2,-3]), -6)

if __name__ == "__main__":
    unittest.main()
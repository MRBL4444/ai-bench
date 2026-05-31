import unittest
from target import average

class TestAverage(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(average([1,2,3,4]), 2.5)
    def test_empty(self):
        self.assertEqual(average([]), 0)
    def test_zero_only(self):
        self.assertEqual(average([0,0,0]), 0)
    def test_mixed(self):
        self.assertEqual(average([-1,0,1]), 0)

if __name__ == "__main__":
    unittest.main()
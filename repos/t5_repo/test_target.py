import unittest
from target import nested_sum

class TestNestedSum(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(nested_sum([[1,2],[3,4]]), 10)
    def test_empty(self):
        self.assertEqual(nested_sum([]), 0)
    def test_single(self):
        self.assertEqual(nested_sum([[5]]), 5)

if __name__ == "__main__":
    unittest.main()
import unittest
from target import multi_edge

class TestMultiEdge(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(multi_edge([]), 0)
    def test_zero_negatives(self):
        self.assertEqual(multi_edge([0,-1,-2]), -3)
    def test_positive(self):
        self.assertEqual(multi_edge([1,2,3]), 6)

if __name__ == "__main__":
    unittest.main()
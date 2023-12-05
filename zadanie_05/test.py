import unittest

from app2 import is_union
from app2 import divide_ranges

class funkcje(unittest.TestCase):
    def test(self):
        self.assertEqual(is_union([-10,10], [11,14]),False, "Should be false")
        self.assertEqual(is_union([1,10], [10,14]),True, "Should be true")
        self.assertEqual(is_union([1,100], [10,14]),True, "Should be true")
        self.assertEqual(is_union([14,100], [10,14]),True, "Should be true")
        self.assertEqual(is_union([13,100], [10,14]),True, "Should be true")
        self.assertEqual(is_union([11,13], [10,14]),True, "Should be true")
        self.assertEqual(is_union([10,14], [10,14]),True, "Should be true")
        
        self.assertEqual(divide_ranges([1,100], [10,14]),[[10, 14], [1, 9], [15, 100]], "Should be true")
        self.assertEqual(divide_ranges([1,12], [10,14]),[[10, 12], [1, 9]], "Should be true")
        self.assertEqual(divide_ranges([12,100], [10,14]),[[12, 14], [15, 100]], "Should be true")
        
        self.assertEqual(divide_ranges([10,14], [10,14]),[[10,14]], "Should be true")
        self.assertEqual(divide_ranges([10,14], [7,15]),[[10,14]], "Should be true")
        
        self.assertEqual(divide_ranges([10,14], [7,15]),[[10,14]], "Should be true")
        self.assertEqual(divide_ranges([57, 69], [53, 60]),[[57,60],[61,69]], "Should be true")
        
        self.assertEqual(divide_ranges([-1,14], [-7,-1]),[[-1,-1],[0,14]], "Should be true")
        self.assertEqual(divide_ranges([-10,-7], [-7,-1]),[[-7,-7],[-10,-8]], "Should be true")
        
if __name__ == '__main__':
    unittest.main()
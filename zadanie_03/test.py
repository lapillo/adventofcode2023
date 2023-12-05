import sys
import unittest

sys.path.append('adventofcode2023/zadanie_03')

from app import find_all_in_text



class Zadanie_pierwsze(unittest.TestCase):
    def test(self):
        self.assertEqual(find_all_in_text("\d+","123..123"), [['123',(0,3)], ['123', (5, 8)]], "Should be [['123',(0,3)], ['123', (5, 8)]]")
        self.assertEqual(find_all_in_text("\d+",".123..123"), [['123',(1,4)], ['123', (6, 9)]], "Should be [['123',(1,4)], ['123', (6, 9)]]")
        self.assertEqual(find_all_in_text("[^0-9\.]",".123.^.123"), [['^',(5,6)]], "Should be [['^',(5,6)]]")
        self.assertEqual(find_all_in_text("[^0-9\.]",".123.^#.123"), [['^',(5,6)],['#',(6,7)]], "Should be [['^',(5,6)],['#',(6,7)]]")
if __name__ == '__main__':
    unittest.main()
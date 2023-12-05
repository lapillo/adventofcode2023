import sys
sys.path.append('/config/workspace/adventofcode2023')

import unittest

from zadanie_02.app import get_game_number
from zadanie_02.app import validate_game_is_possible
from zadanie_02.app import miltiple_min_for_game


class Zadanie_pierwsze(unittest.TestCase):
    
    def testExample(self):
        bag = {"red":12,"green":13,"blue":14}
        self.assertEqual(validate_game_is_possible(bag,"Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"), 1, "Should be 1")  
        self.assertEqual(validate_game_is_possible(bag,"Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue"), 2, "Should be 2")  
        self.assertEqual(validate_game_is_possible(bag,"Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"), 0, "Should be 0")  
        self.assertEqual(validate_game_is_possible(bag,"Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red"), 0, "Should be 0")  
        self.assertEqual(validate_game_is_possible(bag,"Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"), 5, "Should be 5")  
    
    def test_get_game_number(self):
        self.assertEqual(get_game_number("Game 1: 2 blue, 4 green; 7 blue, 1 red, 14 green; 5 blue, 13 green, 1 red; 1 red, 7 blue, 11 green"), "1", "Should be 1")
        self.assertEqual(get_game_number("Game 100: 2 blue, 4 green; 7 blue, 1 red, 14 green; 5 blue, 13 green, 1 red; 1 red, 7 blue, 11 green"), "100", "Should be 1")
        
    def test_validate_game_is_possible(self):
        self.assertEqual(validate_game_is_possible({"red":12,"green":13,"blue":14},"Game 1: 1 blue, 1 green, 1 red"), 1, "Should be 1")  
        self.assertEqual(validate_game_is_possible({"red":0,"green":13,"blue":14},"Game 1: 1 blue, 1 green, 1 red"), 0, "Should be 0")  
        self.assertEqual(validate_game_is_possible({"red":2,"green":1,"blue":1},"Game 1: 1 blue, 1 green, 1 red; 1 red"), 1, "Should be 1")  
        self.assertEqual(validate_game_is_possible({"red":1,"green":1,"blue":1},"Game 1: 1 blue, 1 green, 1 red; 1 red"), 1, "Should be 1")  
        self.assertEqual(validate_game_is_possible({"red":4,"green":1,"blue":1},"Game 2: 1 blue, 1 green, 1 red; 1 red"), 2, "Should be 2")  
        self.assertEqual(validate_game_is_possible({"red":1,"green":1,"blue":1},"Game 2: 1 blue, 1 green, 1 red; 1 red"), 2, "Should be 2")  
        self.assertEqual(validate_game_is_possible({"red":1,"green":1,"blue":1},"Game 2: 1 blue, 1 green, 1 red, 1 red; 1 red"), 0, "Should be 0") 

class Zadanie_drugie(unittest.TestCase):
    
    def testExample(self):
        self.assertEqual(miltiple_min_for_game("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"), 48, "Should be 48")  
        self.assertEqual(miltiple_min_for_game("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue"), 12, "Should be 12") 
        self.assertEqual(miltiple_min_for_game("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"), 1560, "Should be 1560")
        self.assertEqual(miltiple_min_for_game("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red"), 630, "Should be 630")
        self.assertEqual(miltiple_min_for_game("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"), 36, "Should be 36") 
        

if __name__ == '__main__':
    unittest.main()
import unittest

from app import generate_number


class TestNumbers(unittest.TestCase):

    def test(self):
        self.assertEqual(generate_number("one1ssddfsix"), "16", "Should be 16")
        self.assertEqual(generate_number("2one1ssddfsix"), "26", "Should be 26")
        self.assertEqual(generate_number("oneight"), "18", "Should be 18")
        self.assertEqual(generate_number("edf1oneight5"), "15", "Should be 26")

if __name__ == '__main__':
    unittest.main()
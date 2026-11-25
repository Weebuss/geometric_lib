import unittest

from square import area, perimeter

class TestSquare(unittest.TestCase):
    def test_area(self):
        actual = area(5)
        self.assertEqual(actual, 25)

    def test_perimeter(self):
        actual = perimeter(5)
        self.assertEqual(actual, 20)
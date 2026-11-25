import unittest

from rectangle import area, perimeter

class TestRectangle(unittest.TestCase):
    def test_area(self):
        actual = area(3,5)
        self.assertEqual(actual, 15)

    def test_perimeter(self):
        actual = perimeter(3,5)
        self.assertEqual(actual, 16)
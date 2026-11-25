import unittest

from triangle import area, perimeter

class TestTriangle(unittest.TestCase):
    def test_area(self):
        actual = area(4,5)
        self.assertEqual(actual, 10)

    def test_perimeter(self):
        actual = perimeter(3,4,5)
        self.assertEqual(actual, 12)
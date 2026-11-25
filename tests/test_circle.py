import unittest, math

from circle import area, perimeter

class TestCircle(unittest.TestCase):
    def test_area(self):
        actual = area(5)
        self.assertEqual(actual, math.pi*5*5)

    def test_perimeter(self):
        actual = perimeter(5)
        self.assertEqual(actual, 2*math.pi*5)
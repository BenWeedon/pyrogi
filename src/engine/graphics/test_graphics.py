import unittest
from engine.graphics import Color

class TestColor(unittest.TestCase):
    def test_to_tuple(self):
        self.assertEqual(Color(1, 2, 3, 4).to_RGB_tuple(), (1, 2, 3))
        self.assertEqual(Color(1, 2, 3, 4).to_RGBA_tuple(), (1, 2, 3, 4))
        self.assertEqual(Color(1, 2, 3).to_RGBA_tuple(), (1, 2, 3, 255))
    
    def test_equals(self):
        self.assertEqual(Color(1, 2, 3, 4), Color(1, 2, 3, 4))
        self.assertEqual(Color(1, 2, 3), Color(1, 2, 3, 255))
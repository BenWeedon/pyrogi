import unittest
from engine.graphics import Color, LinearGradientPaint
from engine.util.vector import Vec2

class TestColor(unittest.TestCase):
    def test_to_tuple(self):
        self.assertEqual(Color(1, 2, 3, 4).to_RGB_tuple(), (1, 2, 3))
        self.assertEqual(Color(1, 2, 3, 4).to_RGBA_tuple(), (1, 2, 3, 4))
        self.assertEqual(Color(1, 2, 3).to_RGBA_tuple(), (1, 2, 3, 255))
    
    def test_equals(self):
        self.assertEqual(Color(1, 2, 3, 4), Color(1, 2, 3, 4))
        self.assertEqual(Color(1, 2, 3), Color(1, 2, 3, 255))
    
    def test_initialization_errors(self):
        self.assertRaisesRegexp(ValueError, "A Color object cannot contain the float value '1.1'.", Color, 1.1, 2, 3, 4)
        self.assertRaisesRegexp(ValueError, "A Color object cannot contain the float value '2.02'.", Color, 1, 2.02, 3, 4)
        self.assertRaisesRegexp(ValueError, "A Color object cannot contain the float value '3.7'.", Color, 1, 2, 3.7, 4)
        self.assertRaisesRegexp(ValueError, "A Color object cannot contain the float value '4.0'.", Color, 1, 2, 3, 4.0)
        
        self.assertRaisesRegexp(ValueError, 'The parameters to a Color object must be in the range \\[0, 255\\].', Color, -1, 2, 3, 4)
        self.assertRaisesRegexp(ValueError, 'The parameters to a Color object must be in the range \\[0, 255\\].', Color, 256, 2, 3, 4)
        self.assertRaisesRegexp(ValueError, 'The parameters to a Color object must be in the range \\[0, 255\\].', Color, 1, -38, 3, 4)
        self.assertRaisesRegexp(ValueError, 'The parameters to a Color object must be in the range \\[0, 255\\].', Color, 1, 300, 3, 4)
        self.assertRaisesRegexp(ValueError, 'The parameters to a Color object must be in the range \\[0, 255\\].', Color, 1, 2, -3, 4)
        self.assertRaisesRegexp(ValueError, 'The parameters to a Color object must be in the range \\[0, 255\\].', Color, 1, 2, 256, 4)
        self.assertRaisesRegexp(ValueError, 'The parameters to a Color object must be in the range \\[0, 255\\].', Color, 1, 2, 3, -1)
        self.assertRaisesRegexp(ValueError, 'The parameters to a Color object must be in the range \\[0, 255\\].', Color, 1, 2, 3, 500)


class TestPaints(unittest.TestCase):
    def test_linear_gradient(self):
        self._run_linear_gradient_test(
            Color(0, 0, 0, 0), Vec2(0, 0),
            Color(255, 255, 255, 255), Vec2(10, 0),
            Vec2(5, 0), Vec2(5, 0),
            Color(128, 128, 128, 128), Color(128, 128, 128, 128), Color(128, 128, 128, 128), Color(128, 128, 128, 128)
        )
        self._run_linear_gradient_test(
            Color(0, 0, 0, 0), Vec2(0, 0),
            Color(255, 255, 255, 255), Vec2(10, 0),
            Vec2(-2, 0), Vec2(-2, 0),
            Color(51, 51, 51, 51), Color(0, 0, 0, 0), Color(51, 51, 51, 51), Color(0, 0, 0, 0)
        )
        self._run_linear_gradient_test(
            Color(0, 0, 0, 0), Vec2(0, 0),
            Color(255, 255, 255, 255), Vec2(10, 0),
            Vec2(8, 0), Vec2(8, 0),
            Color(204, 204, 204, 204), Color(204, 204, 204, 204), Color(204, 204, 204, 204), Color(204, 204, 204, 204)
        )
        
        self._run_linear_gradient_test(
            Color(0, 0, 0, 0), Vec2(0, 0),
            Color(255, 255, 255, 255), Vec2(10, 0),
            Vec2(10.5, 0), Vec2(10.5, 0),
            Color(242, 242, 242, 242), Color(255, 255, 255, 255), Color(242, 242, 242, 242), Color(255, 255, 255, 255)
        )
        self._run_linear_gradient_test(
            Color(0, 0, 0, 0), Vec2(0, 0),
            Color(255, 255, 255, 255), Vec2(3, 0),
            Vec2(6, 0), Vec2(6, 0),
            Color(0, 0, 0, 0), Color(255, 255, 255, 255), Color(0, 0, 0, 0), Color(255, 255, 255, 255)
        )
        
        self._run_linear_gradient_test(
            Color(0, 0, 0, 0), Vec2(1, 6),
            Color(255, 255, 255, 255), Vec2(3, 17.2),
            Vec2(2, 15), Vec2(0.5, 5),
            Color(203, 203, 203, 203), Color(203, 203, 203, 203), Color(24, 24, 24, 24), Color(0, 0, 0, 0)
        )
        self._run_linear_gradient_test(
            Color(0, 0, 0, 0), Vec2(1, 6),
            Color(255, 255, 255, 255), Vec2(3, 17.2),
            Vec2(4, 23), Vec2(-2, -7),
            Color(123, 123, 123, 123), Color(255, 255, 255, 255), Color(211, 211, 211, 211), Color(0, 0, 0, 0)
        )
        self._run_linear_gradient_test(
            Color(0, 0, 0, 0), Vec2(1, 6),
            Color(255, 255, 255, 255), Vec2(3, 17.2),
            Vec2(6, 30), Vec2(-4.5, -100),
            Color(39, 39, 39, 39), Color(255, 255, 255, 255), Color(190, 190, 190, 190), Color(0, 0, 0, 0)
        )
        self._run_linear_gradient_test(
            Color(0, 0, 0, 0), Vec2(1.2, 12.9),
            Color(255, 255, 255, 255), Vec2(30.8, 3.05),
            Vec2(162.7, -40.7), Vec2(-201.5, 195.2),
            Color(139, 139, 139, 139), Color(255, 255, 255, 255), Color(3, 3, 3, 3), Color(0, 0, 0, 0)
        )
    
    def _run_linear_gradient_test(
            self, color1, position1, color2, position2,
            relative_position, absolute_position,
            t_t_expected_color, f_t_expected_color, t_f_expected_color, f_f_expected_color):
        for pair in [(t_t_expected_color, (True, True)), (f_t_expected_color, (False, True)), (t_f_expected_color, (True, False)), (f_f_expected_color, (False, False))]:
            expected_color = pair[0]
            is_cyclical = pair[1][0]
            is_relative = pair[1][1]
            # test positions/colors in given order
            gradient = LinearGradientPaint(color1, position1, color2, position2, is_cyclical, is_relative)
            self._assertColorEqual(gradient.get_tile_color(relative_position, absolute_position), expected_color)
            # test positions/colors in reverse order
            gradient = LinearGradientPaint(color2, position2, color1, position1, is_cyclical, is_relative)
            self._assertColorEqual(gradient.get_tile_color(relative_position, absolute_position), expected_color)
    
    def _assertColorEqual(self, color1, color2):
        self.assertAlmostEqual(color1.r, color2.r)
        self.assertAlmostEqual(color1.g, color2.g)
        self.assertAlmostEqual(color1.b, color2.b)
        self.assertAlmostEqual(color1.a, color2.a)
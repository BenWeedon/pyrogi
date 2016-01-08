import unittest
from engine.util.vector import Vec2

class TestVec2(unittest.TestCase):
    def test_init(self):
        self.assertEqual(Vec2(1, 4.5), Vec2((1, 4.5)))
        self.assertNotEqual(Vec2(1, 4.5), Vec2((1, 4.51)))
        self.assertEqual(Vec2((2, -3922)), Vec2(2, -3922))
        self.assertNotEqual(Vec2((2, -3922)), Vec2(2, 3922))
    
    def test_vector_multiplication(self):
        self.assertEqual(Vec2(0, 0)*Vec2(1, 5), Vec2(0, 0))
        self.assertEqual(Vec2(1, 5)*Vec2(0, 0), Vec2(0, 0))
        
        self.assertEqual(Vec2(1.0, 1)*Vec2(123456.3020, -987654), Vec2(123456.3020, -987654))
        self.assertEqual(Vec2(123456, -987654)*Vec2(1, 1), Vec2(123456, -987654))
        
        self.assertEqual(Vec2(6, 2)*Vec2(1.5, -6), Vec2(9, -12))
        self.assertEqual(Vec2(1.5, -6)*Vec2(6, 2), Vec2(9, -12))
    
    def test_scalar_multiplication(self):
        self.assertEqual(0*Vec2(1, 594.39), Vec2(0, 0))
        self.assertEqual(Vec2(1, 594.39)*0, Vec2(0, 0))
        
        self.assertEqual(1*Vec2(2893.983, 18320.901290), Vec2(2893.983, 18320.901290))
        self.assertEqual(Vec2(2893.983, 18320.901290)*1, Vec2(2893.983, 18320.901290))
        
        self.assertEqual(2.3939*Vec2(-0.245, 862.254), Vec2(-0.5865055, 2064.1498506))
        self.assertEqual(Vec2(-0.245, 862.254)*2.3939, Vec2(-0.5865055, 2064.1498506))
    
    def test_vector_division(self):
        self.assertEqual(Vec2(0, 0)/Vec2(-12985, 18092.8201), Vec2(0, 0))
        self.assertRaises(ZeroDivisionError, Vec2.__div__, Vec2(-12985, 18092.8201), Vec2(0, 0))
        
        self.assertAlmostEqual_(Vec2(1, 1)/Vec2(3, 5.2), Vec2(0.3333333, 0.1923077))
        self.assertEqual(Vec2(3, 5.2)/Vec2(1, 1), Vec2(3, 5.2))
        
        self.assertAlmostEqual_(Vec2(1184.929, 4)/Vec2(2939.393, -87562.1705), Vec2(0.4031203, -0.000045681828))
        self.assertAlmostEqual_(Vec2(-2939.393, -87562.1705)/Vec2(1184.929, -4), Vec2(-2.48064901, 21890.542625))
    
    def test_scalar_division(self):
        self.assertEqual(0/Vec2(3, 5.9392), Vec2(0, 0))
        self.assertRaises(ZeroDivisionError, Vec2.__div__, Vec2(3, 5.9392), 0)
        self.assertRaises(ZeroDivisionError, Vec2.__rdiv__, Vec2(0, 0), 3)
        
        self.assertAlmostEqual_(1/Vec2(3.2, 9), Vec2(0.3125, 0.1111111))
        self.assertEqual(Vec2(3.2, 9)/1, Vec2(3.2, 9))
        
        self.assertAlmostEqual_(2/Vec2(4, -6.2), Vec2(0.5, -0.3225806))
        self.assertEqual(Vec2(4, 6.2)/-2, Vec2(-2, -3.1))
    
    def test_addition(self):
        self.assertEqual(Vec2(0, 0)+Vec2(34.494, 2.292), Vec2(34.494, 2.292))
        self.assertEqual(Vec2(34.494, 2.292)+Vec2(0, 0), Vec2(34.494, 2.292))
        
        self.assertAlmostEqual_(Vec2(-3, -5.6)+Vec2(-8.54, -0.43), Vec2(-11.54, -6.03))
    
    def test_subtraction(self):
        self.assertEqual(Vec2(0, 0)-Vec2(34.494, 2.292), Vec2(-34.494, -2.292))
        self.assertEqual(Vec2(34.494, 2.292)-Vec2(0, 0), Vec2(34.494, 2.292))
        
        self.assertAlmostEqual_(Vec2(4, 2.1)-Vec2(-6, 1.39), Vec2(10, 0.71))
        self.assertEqual(Vec2(-5.2, -9.6)-Vec2(4, -2.3), Vec2(-9.2, -7.3))
    
    def test_negation(self):
        self.assertEqual(-Vec2(0, 0), Vec2(0, 0))
        self.assertEqual(-Vec2(-1, 1), Vec2(1, -1))
        self.assertEqual(-Vec2(-2.34, 6), Vec2(2.34, -6))
        self.assertEqual(-Vec2(-3.6, -0.945), Vec2(3.6, 0.945))
    
    def test_equals(self):
        self.assertTrue(Vec2(0, 0) == Vec2(0, 0))
        self.assertTrue(Vec2(-2, 5) == Vec2(-2, 5))
        self.assertTrue(Vec2(2.3449, 281.8929203) == Vec2(2.3449, 281.8929203))
        
        self.assertFalse(Vec2(5, 2) == Vec2(-5, 2))
        self.assertFalse(Vec2(1.2364, 2.02) == Vec2(1.2364, 2.0201))
    
    def test_not_equals(self):
        self.assertFalse(Vec2(0, 0) != Vec2(0, 0))
        self.assertFalse(Vec2(-2, 5) != Vec2(-2, 5))
        self.assertFalse(Vec2(2.3449, 281.8929203) != Vec2(2.3449, 281.8929203))
        
        self.assertTrue(Vec2(5, 2) != Vec2(-5, 2))
        self.assertTrue(Vec2(1.2364, 2.02) != Vec2(1.2364, 2.0201))
    
    def test_to_tuple(self):
        self.assertEqual(Vec2(0, 0).to_tuple(), (0, 0))
        self.assertEqual(Vec2(-2.394, 7.00054).to_tuple(), (-2.394, 7.00054))
    
    def assertAlmostEqual_(self, vec1, vec2):
        self.assertAlmostEqual(vec1.x, vec2.x)
        self.assertAlmostEqual(vec1.y, vec2.y)
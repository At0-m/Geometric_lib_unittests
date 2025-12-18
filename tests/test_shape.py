import math
import unittest

from triangle  import area as tri_area,  perimeter as tri_perim
from square    import area as sq_area,   perimeter as sq_perim
from rectangle import area as rect_area, perimeter as rect_perim
from circle    import area as cir_area,  perimeter as cir_perim


class TriangleTestCase(unittest.TestCase):
    def test_area_typical(self):
        self.assertEqual(tri_area(3, 4), 6.0)

    def test_area_zero_height(self):
        self.assertEqual(tri_area(10, 0), 0)

    def test_perimeter_typical(self):
        self.assertEqual(tri_perim(3, 4, 5), 12)

    def test_perimeter_float(self):
        self.assertAlmostEqual(tri_perim(2.5, 2.5, 2.5), 7.5)
    
    def test_area_neg(self):
        with self.assertRaises(ValueError):
            tri_area(-3, 4)
        with self.assertRaises(ValueError):
            tri_area(3, -4)
    
    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            tri_perim(-3, 4, 5)
        with self.assertRaises(ValueError):
            tri_perim(3, -4, 5)
        with self.assertRaises(ValueError):
            tri_perim(3, 4, -5)


class SquareTestCase(unittest.TestCase):
    def test_area_typical(self):
        self.assertEqual(sq_area(5), 25)

    def test_perimeter_typical(self):
        self.assertEqual(sq_perim(5), 20)

    def test_zero_side(self):
        self.assertEqual(sq_area(0), 0)
        self.assertEqual(sq_perim(0), 0)
    
    def test_area_neg(self):
        with self.assertRaises(ValueError):
            sq_area(-5)
    
    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            sq_perim(-5)


class RectangleTestCase(unittest.TestCase):
    def test_area_typical(self):
        self.assertEqual(rect_area(3, 5), 15)

    def test_perimeter_typical(self):
        self.assertEqual(rect_perim(3, 5), 16)

    def test_square_shape(self):
        self.assertEqual(rect_area(4, 4), 16)
        self.assertEqual(rect_perim(4, 4), 16)
    
    def test_area_neg(self):
        with self.assertRaises(ValueError):
            rect_area(-3, 5)
        with self.assertRaises(ValueError):
            rect_area(3, -5)

    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            rect_perim(-3, 5)
        with self.assertRaises(ValueError):
            rect_perim(3, -5)


class CircleTestCase(unittest.TestCase):
    def test_area_typical(self):
        self.assertAlmostEqual(cir_area(3), math.pi * 9)

    def test_perimeter_typical(self):
        self.assertAlmostEqual(cir_perim(3), 2 * math.pi * 3)

    def test_zero_radius(self):
        self.assertEqual(cir_area(0), 0)
        self.assertEqual(cir_perim(0), 0)

    def test_area_neg(self):
        with self.assertRaises(ValueError):
            cir_area(-3)
    
    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            cir_perim(-3)        

if __name__ == "__main__":
  unittest.main()
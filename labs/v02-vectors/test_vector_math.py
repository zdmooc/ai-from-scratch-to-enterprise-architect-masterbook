"""Tests for elementary vector operations."""
import unittest
from vector_math import dot, norm, distance, cosine


class VectorTests(unittest.TestCase):
    def test_dot(self):
        self.assertEqual(dot((1, 2), (3, 4)), 11)
        self.assertEqual(dot((2, -1), (3, 4)), 2)

    def test_norm(self):
        self.assertEqual(norm((3, 4)), 5)

    def test_distance(self):
        self.assertEqual(distance((1, 2), (4, 6)), 5)

    def test_parallel_cosine(self):
        self.assertAlmostEqual(cosine((1, 0), (2, 0)), 1)

    def test_orthogonal_cosine(self):
        self.assertAlmostEqual(cosine((1, 0), (0, 1)), 0)

    def test_zero_cosine_rejected(self):
        with self.assertRaises(ValueError):
            cosine((0, 0), (1, 0))

    def test_different_dimensions_rejected(self):
        with self.assertRaises(ValueError):
            dot((1,), (1, 2))

    def test_empty_input_rejected(self):
        with self.assertRaises(ValueError):
            norm(())

    def test_nonfinite_rejected(self):
        with self.assertRaises(ValueError):
            distance((float("nan"), 1), (1, 2))


if __name__ == "__main__":
    unittest.main()

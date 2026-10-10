"""Unit tests for introductory Python statistics."""
import unittest
from statistics_basics import arithmetic_mean, mean_absolute_error


class BasicsTests(unittest.TestCase):
    def test_mean(self):
        self.assertEqual(arithmetic_mean([2, 4, 6, 8]), 5)

    def test_negative_values(self):
        self.assertEqual(arithmetic_mean([-3, 1, 2]), 0)

    def test_absolute_error(self):
        self.assertAlmostEqual(mean_absolute_error([2, 6, 7], [3, 4, 8]), 4 / 3)

    def test_empty_rejected(self):
        with self.assertRaises(ValueError):
            arithmetic_mean([])

    def test_length_mismatch_rejected(self):
        with self.assertRaises(ValueError):
            mean_absolute_error([1], [1, 2])

    def test_nan_rejected(self):
        with self.assertRaises(ValueError):
            arithmetic_mean([1, float("nan")])

    def test_strings_rejected(self):
        with self.assertRaises(ValueError):
            arithmetic_mean(["4", 6])

    def test_booleans_rejected(self):
        with self.assertRaises(ValueError):
            arithmetic_mean([True, 3])


if __name__ == "__main__":
    unittest.main()

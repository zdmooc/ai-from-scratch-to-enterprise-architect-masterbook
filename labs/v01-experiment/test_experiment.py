"""Unit tests for the finite, synthetic forecast experiment."""
import unittest
from experiment import (
    TRAIN, TEST, average, mean_absolute_error,
    fixed_mean_forecast, rolling_persistence_forecast, evaluate,
)


class ForecastTests(unittest.TestCase):
    def test_training_only_mean(self):
        self.assertEqual(average(TRAIN), 5)

    def test_average_rejects_empty(self):
        with self.assertRaises(ValueError):
            average([])

    def test_fixed_mean_predictions(self):
        self.assertEqual(fixed_mean_forecast(TRAIN, TEST), (5, 5, 5, 5))

    def test_one_step_persistence(self):
        self.assertEqual(rolling_persistence_forecast(TRAIN, TEST), (7, 6, 8, 7))

    def test_computed_mae(self):
        result = evaluate()
        self.assertEqual(result["fixed_mean_mae"], 2.5)
        self.assertEqual(result["rolling_mae"], 1.5)

    def test_protocol_explicit(self):
        self.assertEqual(evaluate()["protocol"], "one_step_ahead_with_observation_after_prediction")

    def test_evaluation_rejects_empty_test(self):
        with self.assertRaises(ValueError):
            evaluate(TRAIN, ())

    def test_mae_rejects_mismatched_lengths(self):
        with self.assertRaises(ValueError):
            mean_absolute_error([1, 2], [1])

    def test_nonfinite_values_rejected(self):
        with self.assertRaises(ValueError):
            evaluate((1, float("nan")), (2,))

    def test_boolean_not_accepted_as_number(self):
        with self.assertRaises(ValueError):
            average([True, 1])

    def test_train_not_mutated(self):
        original = list(TRAIN)
        evaluate(original, TEST)
        self.assertEqual(original, list(TRAIN))

    def test_persistence_does_not_see_same_day(self):
        # Changing a future day's value does NOT change the forecast of that day.
        original = rolling_persistence_forecast(TRAIN, TEST)
        changed = rolling_persistence_forecast(TRAIN, (999, 8, 7, 9))
        self.assertEqual(original[0], changed[0])
        self.assertEqual(changed[1], 999)


if __name__ == "__main__":
    unittest.main()

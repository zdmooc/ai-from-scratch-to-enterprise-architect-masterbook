"""Synthetic one-step-ahead forecasting example for beginners.

The evaluation protocol reveals test observations only *after* each prediction.
No network, machine-learning framework, model or cloud access is required.
"""
from math import fsum, isfinite

TRAIN = (3, 5, 4, 6, 5, 7)
TEST = (6, 8, 7, 9)


def checked(values):
    data = tuple(values)
    if not data:
        raise ValueError("Input must be non-empty")
    if any(isinstance(x, bool) or not isinstance(x, (int, float)) or not isfinite(x) for x in data):
        raise ValueError("Data must be finite numeric observations")
    return data


def average(values):
    data = checked(values)
    return fsum(data) / len(data)


def mean_absolute_error(actual, predicted):
    a, p = checked(actual), checked(predicted)
    if len(a) != len(p):
        raise ValueError("Different lengths cannot be compared")
    return fsum(abs(x - y) for x, y in zip(a, p)) / len(a)


def fixed_mean_forecast(train, test):
    history, evaluation = checked(train), checked(test)
    reference = average(history)
    return tuple(reference for _ in evaluation)


def rolling_persistence_forecast(train, test):
    """Predict each new value using only the latest *previously observed* value."""
    history, evaluation = checked(train), checked(test)
    previous = history[-1]
    forecasts = []
    for actual in evaluation:
        forecasts.append(previous)
        # The real value is revealed only after that day's prediction.
        previous = actual
    return tuple(forecasts)


def evaluate(train=TRAIN, test=TEST):
    history, holdout = checked(train), checked(test)
    mean_predictions = fixed_mean_forecast(history, holdout)
    persistence_predictions = rolling_persistence_forecast(history, holdout)
    return {
        "train_count": len(history),
        "test_count": len(holdout),
        "mean_prediction": average(history),
        "fixed_mean_predictions": mean_predictions,
        "rolling_predictions": persistence_predictions,
        "fixed_mean_mae": mean_absolute_error(holdout, mean_predictions),
        "rolling_mae": mean_absolute_error(holdout, persistence_predictions),
        "protocol": "one_step_ahead_with_observation_after_prediction",
    }


if __name__ == "__main__":
    r = evaluate()
    for key, value in r.items():
        print(f"{key}: {value}")
    print("WARNING: Synthetic 10-value tutorial, no claim of business uplift.")

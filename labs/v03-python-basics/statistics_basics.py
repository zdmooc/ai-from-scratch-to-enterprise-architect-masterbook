"""Introductory statistics, built solely on the Python standard library."""
from math import fsum, isfinite


def _values(items):
    result = tuple(items)
    if not result:
        raise ValueError("At least one value is required")
    if any(isinstance(x, bool) or not isinstance(x, (int, float)) or not isfinite(x) for x in result):
        raise ValueError("Expected finite numeric values")
    return result


def arithmetic_mean(items):
    """Arithmetic mean of a nonempty finite numerical sample."""
    data = _values(items)
    return fsum(data) / len(data)


def mean_absolute_error(actual, predicted):
    """Average absolute deviation of paired observations."""
    observed = _values(actual)
    estimated = _values(predicted)
    if len(observed) != len(estimated):
        raise ValueError("Different input lengths")
    return fsum(abs(a - p) for a, p in zip(observed, estimated)) / len(observed)


if __name__ == "__main__":
    print("mean =", arithmetic_mean([2, 4, 6, 8]))
    print("MAE =", mean_absolute_error([2, 6, 7], [3, 4, 8]))

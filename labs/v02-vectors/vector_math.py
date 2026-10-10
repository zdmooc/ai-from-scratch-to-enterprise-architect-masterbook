"""Vector operations for educational use without external packages."""
from math import fsum, isfinite, sqrt


def _vector(values):
    numbers = tuple(values)
    if not numbers:
        raise ValueError("Empty vector")
    if any(isinstance(x, bool) or not isinstance(x, (int, float)) or not isfinite(x) for x in numbers):
        raise ValueError("Coordinates must be finite numbers")
    return numbers


def _pair(left, right):
    a, b = _vector(left), _vector(right)
    if len(a) != len(b):
        raise ValueError("Dimension mismatch")
    return a, b


def dot(left, right):
    a, b = _pair(left, right)
    return fsum(x * y for x, y in zip(a, b))


def norm(values):
    a = _vector(values)
    return sqrt(fsum(x * x for x in a))


def distance(left, right):
    a, b = _pair(left, right)
    return sqrt(fsum((x - y)**2 for x, y in zip(a, b)))


def cosine(left, right):
    a, b = _pair(left, right)
    denominator = norm(a) * norm(b)
    if denominator == 0:
        raise ValueError("Cosine undefined for zero vectors")
    return dot(a, b) / denominator


if __name__ == "__main__":
    print("dot =", dot((1, 2), (3, 4)))
    print("norm =", norm((3, 4)))
    print("distance =", distance((1, 2), (4, 6)))
    print("cosine =", cosine((1, 0), (2, 0)))

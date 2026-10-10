"""CPU-only educational gradient descent; deterministic synthetic examples."""
from math import fsum, isfinite


def finite_number(value, name):
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not isfinite(value):
        raise ValueError(f"{name} must be a finite number")
    return float(value)


def quadratic_loss(weight, target=4.0):
    w = finite_number(weight, "weight")
    t = finite_number(target, "target")
    result = (w - t) ** 2
    if not isfinite(result):
        raise ValueError("loss overflow")
    return result


def quadratic_gradient(weight, target=4.0):
    return 2 * (finite_number(weight, "weight") - finite_number(target, "target"))


def central_difference(function, value, epsilon=1e-5):
    x = finite_number(value, "value")
    h = finite_number(epsilon, "epsilon")
    if h <= 0 or x + h == x or x - h == x:
        raise ValueError("epsilon cannot resolve a change in x")
    plus = finite_number(function(x + h), "function(x+h)")
    minus = finite_number(function(x - h), "function(x-h)")
    return finite_number((plus - minus) / (2 * h), "estimated gradient")


def descend_quadratic(start=0.0, target=4.0, learning_rate=0.25, steps=3):
    w = finite_number(start, "start")
    t = finite_number(target, "target")
    rate = finite_number(learning_rate, "learning_rate")
    if not 0 < rate < 1:
        raise ValueError("require 0 < learning_rate < 1 for convergence here")
    if isinstance(steps, bool) or not isinstance(steps, int) or not 0 <= steps <= 10000:
        raise ValueError("steps must be an integer in [0, 10000]")
    history = [(w, quadratic_loss(w, t))]
    for _ in range(steps):
        w = finite_number(w - rate * quadratic_gradient(w, t), "weight update")
        history.append((w, quadratic_loss(w, t)))
    return tuple(history)


def _dataset(xs, ys):
    features, targets = tuple(xs), tuple(ys)
    if not features or len(features) != len(targets):
        raise ValueError("non-empty input and target sequences of equal size required")
    return (tuple(finite_number(x, "x") for x in features),
            tuple(finite_number(y, "y") for y in targets))


def linear_mse_and_gradient(xs, ys, weight, bias):
    """For predictions weight*x+bias, return MSE, dMSE/dweight, dMSE/dbias."""
    xx, yy = _dataset(xs, ys)
    w, b = finite_number(weight, "weight"), finite_number(bias, "bias")
    errors = tuple(w * x + b - y for x, y in zip(xx, yy))
    if not all(isfinite(e) for e in errors):
        raise ValueError("prediction overflow")
    n = len(errors)
    loss = finite_number(fsum(e * e for e in errors) / n, "MSE")
    dw = finite_number(2 * fsum(e * x for e, x in zip(errors, xx)) / n, "weight gradient")
    db = finite_number(2 * fsum(errors) / n, "bias gradient")
    return loss, dw, db


def train_line(xs, ys, rate=0.05, steps=2000):
    xx, yy = _dataset(xs, ys)
    lr = finite_number(rate, "rate")
    if lr <= 0:
        raise ValueError("rate must be strictly positive")
    if isinstance(steps, bool) or not isinstance(steps, int) or not 1 <= steps <= 10000:
        raise ValueError("steps must be an integer in [1, 10000]")
    w = b = 0.0
    for _ in range(steps):
        _, dw, db = linear_mse_and_gradient(xx, yy, w, b)
        w = finite_number(w - lr * dw, "updated weight")
        b = finite_number(b - lr * db, "updated bias")
    return w, b, linear_mse_and_gradient(xx, yy, w, b)[0]


if __name__ == "__main__":
    print("quadratic:", descend_quadratic())
    print("line:", train_line((0, 1, 2, 3), (1, 3, 5, 7)))

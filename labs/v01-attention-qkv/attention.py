"""Tiny, CPU-only, scaled dot-product attention; pedagogical, not production."""
from math import exp, fsum, isfinite, sqrt


def _matrix(values, name):
    try:
        rows = tuple(tuple(row) for row in values)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{name} must be a rectangular matrix") from exc
    if not rows or not rows[0] or any(len(row) != len(rows[0]) for row in rows):
        raise ValueError(f"{name} must be rectangular and non-empty")
    if any(isinstance(x, bool) or not isinstance(x, (int,float)) or not isfinite(x)
           for row in rows for x in row):
        raise ValueError(f"{name} must contain finite real coordinates")
    return rows


def stable_softmax(scores):
    values = tuple(scores)
    if not values or any(isinstance(x, bool) or not isinstance(x,(int,float)) or not isfinite(x) for x in values):
        raise ValueError("scores must be non-empty finite reals")
    largest = max(values)
    exps = tuple(exp(value - largest) for value in values)
    total = fsum(exps)
    return tuple(e / total for e in exps)


def causal_mask(length):
    if isinstance(length, bool) or not isinstance(length, int) or length < 1:
        raise ValueError("causal mask length must be a positive integer")
    return tuple(tuple(j <= i for j in range(length)) for i in range(length))


def attention(queries, keys, values, mask=None):
    """Return (attention weights, weighted value rows).

    Rows in Q/K have equal d_k. K/V have equal token counts.
    mask[q][k] is True for an allowed key and False for excluded keys.
    """
    q = _matrix(queries, "Q")
    k = _matrix(keys, "K")
    v = _matrix(values, "V")
    if len(q[0]) != len(k[0]) or len(k) != len(v):
        raise ValueError("Q/K dimension or K/V row count mismatch")
    if mask is None:
        permitted = tuple((True,) * len(k) for _ in q)
    else:
        try:
            permitted = tuple(tuple(row) for row in mask)
        except (TypeError, ValueError) as exc:
            raise ValueError("mask must be a boolean matrix") from exc
        if len(permitted) != len(q) or any(len(row) != len(k) for row in permitted):
            raise ValueError("mask shape mismatch")
        if any(type(value) is not bool for row in permitted for value in row):
            raise ValueError("mask must contain booleans")
    weights, output = [], []
    for query, allowed in zip(q, permitted):
        if not any(allowed):
            raise ValueError("a query has no permitted keys")
        scores = [fsum(a*b for a,b in zip(query,key)) / sqrt(len(query))
                  for key in k]
        if not all(isfinite(score) for score in scores):
            raise ValueError("attention scores overflow")
        available = [score for score, use in zip(scores, allowed) if use]
        probs = iter(stable_softmax(available))
        row_weights = tuple(next(probs) if use else 0.0 for use in allowed)
        weighted = tuple(fsum(w * value[col] for w,value in zip(row_weights,v))
                         for col in range(len(v[0])))
        if not all(isfinite(x) for x in weighted):
            raise ValueError("attention outputs overflow")
        weights.append(row_weights)
        output.append(weighted)
    return tuple(weights), tuple(output)


if __name__ == '__main__':
    q = ((1, 0),)
    k = ((1, 0), (0, 1))
    v = ((2, 0), (0, 2))
    print('weights, output:', attention(q,k,v))

"""Scoring helpers."""


def score_span(span, weights):
    return sum(span[i] * weights[i] for i in range(len(weights)))

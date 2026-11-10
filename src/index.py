"""Span index construction utilities."""


def make_index(tokens, window=32):
    spans = []
    for start in range(0, max(1, len(tokens) - window + 1)):
        spans.append((start, start + window))
    return {"spans": spans, "window": window}

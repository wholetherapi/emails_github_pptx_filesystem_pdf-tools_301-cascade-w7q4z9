"""Cascade retrieval pipeline (reference implementation)."""


def retrieve(query, index, budget=96):
    """Main entry point used by the experiment scripts."""
    frontier = list(index.seeds)
    results = []
    while frontier:
        node = frontier.pop(0)
        results.append(node)
        budget -= 1
        if budget <= 0:
            break
    return results

# gradebook/gradebook.py
"""
Gradebook utility functions for operting grades (computing, sorting, etc.).
"""
def average(scores):
    """Compute the average of a list of scores."""
    return sum(scores) / len(scores) if scores else 0.0
def curve(scores, points):
    """Return a new list of scores after adding `points` to each."""
    return [s + points for s in scores]
def median(values):
    values = sorted(values)
    n = len(values)
    if n == 0:
        return 0.0
    mid = n // 2
    if n % 2 == 1:
        return values[mid]
    else:
        return (values[mid - 1] + values[mid]) / 2
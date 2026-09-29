# tests/test_gradebook.py
"""
Basic tests for gradebook functions.
"""

from gradebook.gradebook import average, curve, median
def test_average_basic():
    assert average([100, 80, 90]) == 90.0
def test_average_empty():
    assert average([]) == 0.0
def test_curve_basic():
    assert curve([70, 80, 90], 5) == [75, 85, 95]
def test_median_basic():
    assert median([1, 3, 2]) == 2
    assert median([1, 2, 3, 4]) == 2.5
    assert median([]) == 0.0
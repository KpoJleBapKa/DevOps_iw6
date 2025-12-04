import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import add, is_even

def test_add():
    assert add(2, 3) == 5
    assert add(0, 0) == 0
    assert add(-5, 3) == -2

@pytest.mark.parametrize("value, expected", [
    (0, True),
    (2, True),
    (-4, True),
    (1, False),
    (-3, False),
    (100, True),
    (101, False)
])
def test_is_even(value, expected):
    assert is_even(value) == expected

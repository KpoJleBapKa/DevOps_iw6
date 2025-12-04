import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import add, is_even

@pytest.fixture
def sample_numbers():
    return [0, 2, 4, 6, 8, 10, -2, -4]

def test_is_even_large_odd():
    assert is_even(99999999) is False

def test_all_even(sample_numbers):
    for n in sample_numbers:
        assert is_even(n) is True

def test_add():
    assert add(2, 3) == 5
    assert add(0, 0) == 0
    assert add(-5, 3) == -2

def test_add_large_numbers():
    assert add(1_000_000, 2_000_000) == 3_000_000
    assert add(-1_000_000, 500_000) == -500_000

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

@pytest.mark.parametrize("a, b, expected", [
    (1, -1, 0),
    (100, -50, 50),
    (7, 3, 10),
    (-10, -5, -15),
])

def test_add_parametrized(a, b, expected):
    assert add(a, b) == expected

##pytest -q
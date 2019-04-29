import pytest
from factorial import factorial

def test_factorial():
    result = factorial(5)
    assert result == 120

def test_factorial_zero():
    result = factorial(0)
    assert result == 1

def test_negative_factorial():
    with pytest.raises(ValueError):
        factorial(-1)

def test_illegal_characters():
    with pytest.raises(ValueError):
        factorial(10.5)
    
import pytest
import math
from src.math_utils import square_root, logarithm


def test_square_root():
    assert square_root(16) == 4.0
    assert square_root(0) == 0.0
    assert square_root(2) == pytest.approx(math.sqrt(2))
    assert square_root(0.25) == 0.5


def test_square_root_negative():
    with pytest.raises(ValueError, match="Cannot take square root of a negative number"):
        square_root(-1)
    with pytest.raises(ValueError, match="Cannot take square root of a negative number"):
        square_root(-0.001)


def test_logarithm_base10():
    assert logarithm(100, 10) == pytest.approx(2.0)
    assert logarithm(1000, 10) == pytest.approx(3.0)
    assert logarithm(1, 10) == pytest.approx(0.0)


def test_logarithm_natural():
    assert logarithm(math.e) == pytest.approx(1.0)
    assert logarithm(1) == pytest.approx(0.0)


def test_logarithm_base2():
    assert logarithm(8, 2) == pytest.approx(3.0)
    assert logarithm(1024, 2) == pytest.approx(10.0)


def test_logarithm_invalid_input():
    with pytest.raises(ValueError, match="Cannot take log of zero or negative number"):
        logarithm(0)
    with pytest.raises(ValueError, match="Cannot take log of zero or negative number"):
        logarithm(-5)


def test_logarithm_invalid_base():
    with pytest.raises(ValueError, match="Logarithm base must be positive"):
        logarithm(10, 1)
    with pytest.raises(ValueError, match="Logarithm base must be positive"):
        logarithm(10, 0)
    with pytest.raises(ValueError, match="Logarithm base must be positive"):
        logarithm(10, -2)

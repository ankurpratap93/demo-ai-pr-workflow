"""
Math utility functions — extends calculator with sqrt and log operations.
"""
import math


def square_root(a: float) -> float:
    """Return sqrt(a). Raises ValueError for negative input."""
    if a < 0:
        raise ValueError("Cannot take square root of a negative number")
    return math.sqrt(a)


def logarithm(a: float, base: float = math.e) -> float:
    """Return log_base(a). Defaults to natural log (e)."""
    if a <= 0:
        raise ValueError("Cannot take log of zero or negative number")
    if base <= 0 or base == 1:
        raise ValueError("Logarithm base must be positive and not equal to 1")
    return math.log(a, base)

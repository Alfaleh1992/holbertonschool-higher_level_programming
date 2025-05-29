#!/usr/bin/python3
"""
add_integer(a, b=98)

Adds two numbers and returns the result.

Example
-------
>>> add_integer(5, 10)
15
"""


def add_integer(a, b=98):
    """
    Add two integers or floats.

    Args:
        a: first number (int or float)
        b: second number (int or float), defaults to 98

    Returns:
        int: the sum of a and b, after converting floats to ints

    Raises:
        TypeError: if a or b is not an int or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Convert floats to ints before addition, as requested
    a = int(a) if isinstance(a, float) else a
    b = int(b) if isinstance(b, float) else b
    return a + b

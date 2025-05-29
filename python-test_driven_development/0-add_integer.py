#!/usr/bin/python3
"""
    Function adds two integers.

    Example:
       a = 5
       b = 10

       add_integer(a, b)

       15
"""


def add_integer(a, b=98):
    """
        Args:
            a: first integer
            b: second integer

        Returns:
            Sum of the two integers
    """
    if not isinstance(a, (float, int)):
        if a is not None:
            raise TypeError("a must be an integer")
        raise ValueError("a must be an integer")

    if not isinstance(b, (float, int)):
        if b is not None:
            raise TypeError("b must be an integer")
        raise ValueError("b must be an integer")

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return a + b
  
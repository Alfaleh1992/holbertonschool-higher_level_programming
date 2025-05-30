#!/usr/bin/python3
"""1-square.py: Defines a class Square that represents a square."""


class Square:
    """Represents a square by its size.

    Attributes:
        __size (int): The size of the square (private).
    """

    def __init__(self, size):
        """Initialize a new square.

        Args:
            size (int): The size of the square.
        """
        self.__size = size

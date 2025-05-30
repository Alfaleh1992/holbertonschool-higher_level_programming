#!/usr/bin/python3
"""5-square.py: Defines a class Square with area and print method."""


class Square:
    """Represents a square with size, area computation, and print capability."""

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square.

        Returns:
            int: The current size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation.

        Args:
            value (int): The new size.

        Raises

#!/usr/bin/python3
"""5-square.py: Defines a class Square that prints a square with '#'."""


class Square:
    """Represents a square with size, area, and print functionality."""

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int): Size of the square.

        Raises:
            TypeError: If size is not an int.
            ValueError: If size < 0.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the current size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the current size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square using '#' characters."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)

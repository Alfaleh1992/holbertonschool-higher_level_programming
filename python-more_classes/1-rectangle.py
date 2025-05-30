#!/usr/bin/python3
"""1-rectangle.py: Defines a class Rectangle with validated attributes."""


class Rectangle:
    """Represents a rectangle with width and height."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The rectangle width (default 0).
            height (int): The rectangle height (default 0).
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width with validation.

        Args:
            value (int): The new width.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is negative.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height with validation.

        Args:
            value (int): The new height.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is negative.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

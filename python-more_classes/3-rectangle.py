#!/usr/bin/python3
"""Defines a class Rectangle with string and reproducible representations."""


class Rectangle:
    """Represents a rectangle defined by width and height."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): Rectangle width (default 0).
            height (int): Rectangle height (default 0).
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle with validation.

        Args:
            value (int): New width.

        Raises:
            TypeError:

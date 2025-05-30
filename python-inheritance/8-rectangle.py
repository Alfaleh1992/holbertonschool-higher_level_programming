#!/usr/bin/python3
"""Defines class Rectangle that inherits from BaseGeometry"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Initialize rectangle with width and height
        Both must be validated positive integers."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """String representation of the Rectangle instance."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

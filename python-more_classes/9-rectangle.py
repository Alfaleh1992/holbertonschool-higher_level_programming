#!/usr/bin/python3
"""This is the 'rectangle' module.

This module provides a Rectangle class.
"""


class Rectangle:
    """Rectangle class with attributes width and height,
    and methods area, perimeter, print, repr, del, str, eq, and gt.
    Class attribute number_of_instances to keep track of # of instances,
    class attribute print_symbol that is used for visual output,
    static method bigger_or_equal that returns biggest rectangle,
    and class method square that returns a new Square.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        rows = []
        for i in range(self.__height):
            rows.append(str(self.print_symbol) * self.__width)
        return "\n".join(rows)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)


class Square(Rectangle):
    """Square inherits from Rectangle. Sets width and height to same size."""

    def __init__(self, size):
        super().__init__(size, size)

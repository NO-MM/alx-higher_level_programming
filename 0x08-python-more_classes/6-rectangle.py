#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle:
    """Representation of a Rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializes the rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter for the private instance attribute width"""
        return self._width

    @width.setter
    def width(self, value):
        """Setter for the private instance attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """Getter for the private instance attribute height"""
        return self._height

    @height.setter
    def height(self, value):
        """Setter for the private instance attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        """Returns the areas of the rectangle"""
        return self._width * self._height

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self._width == 0 or self._height == 0:
            return 0
        return (self._width * 2) + (self._height * 2)

    def __str__(self):
        """Returns printable string representation of the rectangle"""
        string = ""
        if self._width != 0 and self._height != 0:
            string += "\n".join("#" * self._width for j in range(self._height))
            return string

    def __repr__(self):
        """Returns a string represantation of the rectangle for production"""
        return "Rectangle({:d}, {:d})".format(self._width, self._height)

    def __del__(self):
        """Print a message for every deletion of a rectangle"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

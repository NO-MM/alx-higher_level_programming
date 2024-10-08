#!/usr/bin/python3
"""Defines a class Rectangle"""

class Rectangle:
    """Representation of a Rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes the rectangle"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """Getter for the private instance attribute width"""
        return self._width

    @width.setter
    def width(self, value):
        """setter for the private instance attribute width"""
        if type(value) is not int:
            raise TypeEror("width must be an integer")
        if value < 0:
            raise valueError("height mut be >= 0")
        self._height = value

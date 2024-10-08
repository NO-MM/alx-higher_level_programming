#!/usr/bin/python3
"""Define a square class"""


class Square:
    """Representation of a square class"""

    def __init__(self, size=0):
        """Instantiation with size for our object initialization"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        """Getter for the private attribute size"""
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """Setter property"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Method that returns the current square area"""
        return (self.__size * self.__size)

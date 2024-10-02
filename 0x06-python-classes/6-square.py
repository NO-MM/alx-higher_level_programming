#!/usr/bin/python3
"""Define a square class"""
class Square:
    """Representation of a square class"""

    def __init__(self, size=0, position=(0, 0)):
        """Instantiation with size for our object initialization"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position

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

    def my_print(self):
        """Print rep of square with # character"""
        if self.__size == 0:
            print()

        for i in range(self.__position[1]):
            [print(" ", end="") for j in range(self.__size)]
            print("#", end="")

    """Private attribute"""
    @property
    def position(self):
        """Private instance attribute: position"""
        return self.__position

    @position.setter
    def position(self, value):
        """The setter for position"""
        if not isinstance(value, tuple) or \
           len(value) != 2 or \
           not all(isinstance(num, int) for num in value) or \
           not all(num >= 0 for num in value):
           raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

#!/usr/bin/python3
"""Defines a class Rectangle"""

class Rectangle:
    """Representation of a Rectangle"""

    number_of_instances = 0

    '''int: The number of active instances.'''

    print_symbol ='#'
    '''type: Print symbol, can be anytype.'''

    def __init__(self, width=0, height=0):
        """Constructor

        Args:
            width: The width of rectangle.
            height: The height of rectangle.
        """
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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the bigger of two rectangles:

        Args:
            rect_1: The first rectangle.
            rect_2: The second rectangle.

        Raises:
            TypeError: If rect_1, rect_2 are not instances of rectangle.
       
        Returns:
            The rectangle with the larger area.                                   
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1, must be an instance of rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2, must be an instance of rectangle")


        if rect_2.area() > rect_1.area():
            return rect_2


        return rect_1

    def __str__(self):
        """Returns string representation"""
        if not self.width or not self.height:
            return ""
        return ((str(self.print_symbol) * self.width + "\n") * self.height)[:-1]

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self._width == 0 or self._height == 0:
            return 0
        return (self._width *2) + (self._height *2)

    def __repr__(self):
        """Returns a string represantation of the rectangle for production"""
        return"Rectangle({:d}, {:d})".format(self._width, self._height)

    def __del__(self):
        """Called instance deletation"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

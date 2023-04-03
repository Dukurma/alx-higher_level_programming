#!/usr/bin/python3
"""Area & Perimeter"""


class Rectangle:
    """Defining/initializing the  rectangle"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter, for the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter, for width mutation"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter, for
        the rectangle height

        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """instance method that returns
        the rectangle area

        """
        rectangle_area = self.__height * self.__width
        return rectangle_area

    def perimeter(self):
        """instance method that returns the
        rectangle perimeter

        """
        if self.__width == 0 or self.__height == 0:
            return (0)
        rectangle_params = ((2 * self.__height) + (2 * self.__width))
        return rectangle_params

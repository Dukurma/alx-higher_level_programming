#!/usr/bin/python3
"""defining a rectangle"""


class Rectangle:
    """class created thus defining the instant variables """
    
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
    """Get the width of the rectangle
    """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter, for setting"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get
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

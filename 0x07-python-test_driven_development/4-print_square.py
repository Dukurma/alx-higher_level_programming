#!/usr/bin/python3
"""Creates a square using print function."""


def print_square(size):
    """Print a square with a special character.

    Argments:
        size (int): The height/width of the square.
    Errors:
        TypeError: If size is not an integer.
        ValueError: If size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")

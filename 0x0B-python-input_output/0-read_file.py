#!/usr/bin/python3
"""Create a text file-reading function."""


def read_file(filename=""):
    """Print all the contents of a UTF8 text file to stdout."""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")

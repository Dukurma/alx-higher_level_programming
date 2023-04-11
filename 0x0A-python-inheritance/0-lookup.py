#!/usr/bin/python3
"""Creates an object attribute lookup function."""


def lookup(obj):
    """Return a list of available object's  attributes."""
    return (dir(obj))

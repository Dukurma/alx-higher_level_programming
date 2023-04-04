#!/usr/bin/python3
"""Creates a locked class."""


class LockedClass:
    """
    Doesn't allow  the user from instantiating new LockedClass attributes
    for anything but attributes called 'first_name'.
    """

    __slots__ = ["first_name"]

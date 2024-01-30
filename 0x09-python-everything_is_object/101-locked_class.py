#!/usr/bin/python3
# 101-locked_class.py

"""Define locked class."""


class LockedClass:
    """
    user cant be instantiating new LockedClass attributes
    for anything but attributes called 'first_name'.
    """

    __slots__ = ["first_name"]

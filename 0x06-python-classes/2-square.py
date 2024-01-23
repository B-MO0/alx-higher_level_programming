#!/usr/bin/python3
"""define my class """


class Square:
    """ my class atrs """
    def __init__(self, size):
        """initialize atrs"""
        if type(size) is int:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.size = size
        else:
            raise ValueError('size must be an integer')

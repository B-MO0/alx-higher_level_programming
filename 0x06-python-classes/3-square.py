#!/usr/bin/python3
"""define my class """


class Square:
    """ my class atrs """
    def __init__(self, size=0):
        """initialize atrs"""
        if type(size) is int:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError('size must be an integer')

    def area(self):
        """
        calculates the area of sqr
        Returns:
            the area of square
        """
        return self.__size ** 2

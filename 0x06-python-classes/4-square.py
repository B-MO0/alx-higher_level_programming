"""define my class """


class Square:
    """ my class atrs """
    def __init__(self, size=0):
        """initialize atrs"""
        self.__size = size
        
    def area(self):
        """
        calculates the area of sqr
        Returns:
            the area of square
        """
        return self.__size ** 2
    @property
    def size(self):
        """ getter of size """
        return self.__size
    @size.setter
    def size(self, value):
        """ setter of size """
        if type(value) is int:
            if value < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = value
        else:
            raise TypeError('size must be an integer')

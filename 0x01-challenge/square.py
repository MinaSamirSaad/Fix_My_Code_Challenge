#!/usr/bin/python3
""" Square class
"""

class Square():
    """ Square class """
    side = 0

    def __init__(self, *args, **kwargs):
        """ Constructor """
        if args:
            self.side = args[0]
            return
        if kwargs:
            if 'side' in kwargs:
                self.side = kwargs['side']
                return
        self.side = 0

    def area_of_my_square(self):
        """ Area of the square """
        return self.side * self.side

    def PermiterOfMySquare(self):
        return self.side * 4

    def __str__(self):
        return "{}/{}".format(self.side, self.side)

if __name__ == "__main__":

    s = Square(side=10)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())

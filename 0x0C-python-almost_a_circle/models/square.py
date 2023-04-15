#!/usr/bin/python3
"""
this is the square module
this module define a class
Square which inherits from Rectangle
"""


from models.rectangle import Rectangle
"""this imports the rectangle module"""


class Square(Rectangle):
    """defines the class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """initializes the attributes"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """returns a string representation in a format"""
        s = "[Square] ({:d}) {:d}/{:d} - {:d}"
        r = s.format(self.id, self.x, self.y, self.size)
        return r

    @property
    def size(self):
        """retrieves the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """sets the value of size"""
        self.width = value
        self.height = value

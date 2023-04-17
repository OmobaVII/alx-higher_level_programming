#!/usr/bin/python3
"""
this is the square module
this module define a class

Square which inherits from Rectangle
initializes superclass id, width as size or height as size
Contains public attribute size
displays the square using #
prints [Square] (id) x/y - size
Updates attributes args and kwargs
Returns dictionary representation of attributes
"""


from models.rectangle import Rectangle
"""this imports the rectangle module"""


class Square(Rectangle):
    """defines the class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """initializes the attributes"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """returns a string representation in a format"""
        s = "[Square] ({:d}) {:d}/{:d} - {:d}"
        r = s.format(self.id, self.x, self.y, self.width)
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

    def update(self, *args, **kwargs):
        if args:
            attrs = ['id', 'size', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns a dictionary representation"""
        s = {}
        s['id'] = self.id
        s['size'] = self.width
        s['x'] = self.x
        s['y'] = self.y
        return s

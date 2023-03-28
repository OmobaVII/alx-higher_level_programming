#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position
        @property
        def size(self):
            return self.__size
        @size.setter
        def size(self, value):
            if type(size) is not int:
                raise TypeError("size must be an integer")
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = value
        @property
        def position(self):
            return self.__property
        @position.setter
        def position(self, value):
            if type(position) is not tuple or len(position) != 2:
                raise TypeError("position must be a tuple of 2 positive integer")
            if type(position[0]) is not int or position[0] < 0:
                raise TypeError("position must be a tuple of 2 positive integer")
            if type(position[1]) is not int or position[1] < 0:
                raise TypeError("position must be a tuple of 2 positive integer")
            self.__position = value
        def area(self):
            return (self.__size ** 2)
        def my_print(self):
            a = 0
            b = 0
            position = list(self.__position)
            while b < self.__size:
                while position[1] > 0:
                    print()
                    position[1] -= 1
                while position[0] > 0:
                    print(" ", end="")
                    position[0] -= 1
                while a < self.__size:
                    print("#", end="")
                    a += 1
                a = 0
                b += 1
                position[0] = self._position[0]
                print()
            if self.__size == 0:
                print()
    def __value__(self):
        a = 0
        b = 0
        pos = list(self.__position)
        value = ""
        if self.__size == 0:
            return value
        while b < self.__size:
            while pos[1] > 0:
                value += "\n"
                pos[1] -= 1
            while pos[0] > 0:
                value += " "
                pos[0] -= 1
            while a < self.__size:
                value += "#"
                a += 1
            a = 0
            b += 1
            pos[0] = self.__position[0]
            value += "\n"
        return value

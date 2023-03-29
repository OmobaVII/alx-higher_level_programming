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
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    @property
    def position(self):
        return self.__property
    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integer")
        if type(value[0]) is not int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integer")
        if type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value
    def area(self):
        return (self.__size ** 2)
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for row in range(self._position[1]):
                print()
            for i in range(self.__size):
                for col in range(self.__position[0]):
                    print(" ", end="")
                for j in range (self.__size):
                    print("#", end="")
                print()
    def __str__(self):
        a = 0
        b = 0
        pos = list(self.__position)
        s = ""
        if self.__size == 0:
            return s
        while b < self.__size:
            while pos[1] > 0:
                s += "\n"
                pos[1] -= 1
            while pos[0] > 0:
                s += " "
                pos[0] -= 1
            while a < self.__size:
                s += "#"
                a += 1
            a = 0
            b += 1
            pos[0] = self.__position[0]
            if b < self.__size:
                s += "\n"
        return s

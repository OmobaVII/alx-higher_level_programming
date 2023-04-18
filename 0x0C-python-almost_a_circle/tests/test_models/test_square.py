#!/usr/bin/python3
"""
Unittest for Square
"""


import pep8
import unittest
from io import StringIO
from contextlib import redirect_stdout
from models import square
Square = square.Square


class TestSquare(unittest.TestCase):
    """test for the class Square"""
    def test_pep8_Square(self):
        """test pep8"""
        style = pep8.StyleGuide(quit=True)
        files = ["models/square.py", "tests/test_models/test_square.py"]
        check = style.check_files(files)
        self.assertEqual(check.total_errors, 0, "Need to fix Pep8")

    def test_attribute(self):
        """test the attributes of the square"""
        s1 = Square(5)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.area(), 25)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        s3 = Square(3, 1, 3)
        self.assertEqual(s3.size, 3)
        self.assertEqual(s3.x, 1)
        self.assertEqual(s3.y, 3)
        self.assertTrue(s3.id is not None)

    def test_validation(self):
        """tests the inputs validation"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("a")
            Square((3, 5))
            Square([2, 4])
            Square({"a": 4})
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(4, -2)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(4, 2, -2)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "2")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, "3")

    def test_private(self):
        """test if private attributes are private"""
        with self.assertRaises(AttributeError):
            print(Square.__size)
            print(Square.__x)
            print(Square.__y)

    def test_too_many_few(self):
        """test too many and too few"""
        with self.assertRaises(TypeError):
            Square(8, 2, 4, 2, 1)
        with self.assertRaises(TypeError):
            Square()
        with self.assertRaises(TypeError):
            Square(None)

    def test_Square(self):
        """tests if the class is actually square"""
        self.assertEqual(type(Square(3)), Square)

    def test_area(self):
        """tests the area of the square"""
        self.assertEqual(Square(2).area(), 4)
        self.assertEqual(Square(2, 3, 2, 1).area(), 4)

    def test_display(self):
        """tests the display method"""
        with StringIO() as display, redirect_stdout(display):
            Square(2).display()
            s = display.getvalue()
        self.assertEqual(s, "##\n##\n")
        with StringIO() as display, redirect_stdout(display):
            Square(2, 2, 2).display()
            s = display.getvalue()
        self.assertEqual(s, "\n\n  ##\n  ##\n")

    def test_str(self):
        """tests the str method"""
        s1 = Square(3, 1, 2, 12)
        self.assertEqual(str(s1), "[Square] (12) 1/2 - 3")

    def test_update(self):
        """tests the update method"""
        s1 = Square(3, 1, 2, 12)
        self.assertEqual(str(s1), "[Square] (12) 1/2 - 3")
        s1.update(4)
        self.assertEqual(str(s1), "[Square] (4) 1/2 - 3")
        s1.update(id=10, size=3, x=2, y=4)
        self.assertEqual(str(s1), "[Square] (10) 2/4 - 3")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s1.update(size="3")

    def test_to_dictionary(self):
        """tests the dictionary method"""
        s1 = Square(10, 2, 1, 7)
        s1_dictionary = s1.to_dictionary()
        string = "{'id': 7, 'size': 10, 'x': 2, 'y': 1}"
        self.assertEqual(str(s1_dictionary), string)

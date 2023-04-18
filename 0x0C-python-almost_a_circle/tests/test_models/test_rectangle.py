#!/usr/bin/python3
"""
Unittest for Rectangle Class
"""

import pep8
import os
import unittest
from io import StringIO
from contextlib import redirect_stdout
from models import rectangle
Rectangle = rectangle.Rectangle


class TestRectangle(unittest.TestCase):
    """Test for class Rectangle"""
    def test_pep8_rectangle(self):
        """test for pep8"""
        style = pep8.StyleGuide(quit=True)
        files = ["models/rectangle.py", "tests/test_models/test_rectangle.py"]
        check = style.check_files(files)
        self.assertEqual(check.total_errors, 0, "Need to fix Pep8")

    def test_attribute(self):
        """test the rectangle attributes"""
        r1 = Rectangle(4, 5, 1, 3, 89)
        self.assertEqual(r1.width, 4)
        self.assertEqual(r1.height, 5)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.y, 3)
        self.assertEqual(r1.id, 89)
        r2 = Rectangle(4, 5)
        self.assertEqual(r2.width, 4)
        self.assertEqual(r2.height, 5)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)
        self.assertTrue(r2.id is not None)

    def test_validation(self):
        """test the inputs validation"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("a", 4)
            Rectangle((4, 5), 5)
            Rectangle([2, 4], 3)
            Rectangle({"a": 4}, 3)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, "a")
            Rectangle(8, [2, 5])
            Rectangle(4, {"a": 3})
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 7, "a", 3, 5)
            Rectangle(3, 7, [1, 3], 3, 5)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 7, 4, "3", 5)
            Rectangle(3, 7, 4, {"s": 3}, 5)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 3)
            Rectangle(-2, 3)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(3, -2)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(3, 7, -1, 3, 5)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(3, 7, 4, -3, 5)

    def test_private(self):
        """test if private attributes are private"""
        with self.assertRaises(AttributeError):
            print(Rectangle.__width)
            print(Rectangle.__height)
            print(Rectangle.__x)
            print(Rectangle.__y)

    def test_toomany_and_toofew(self):
        """tests for many and few arguments"""
        with self.assertRaises(TypeError):
            Rectangle(1, 4, 6, 2, 5, 7, 8, 3)
            Rectangle(5)
            Rectangle()
            Rectangle(None)

    def test_Rectangle(self):
        """tests if the class if actually Rectangle"""
        self.assertEqual(type(Rectangle(2, 3)), Rectangle)

    def test_area(self):
        """tests the area of the rectangle"""
        self.assertEqual(Rectangle(2, 4).area(), 8)
        self.assertEqual(Rectangle(3, 5, 1, 5, 3).area(), 15)

    def test_display(self):
        """tests the diplay method"""
        with StringIO() as display, redirect_stdout(display):
            Rectangle(2, 3).display()
            r = display.getvalue()
        self.assertEqual(r, "##\n##\n##\n")
        with StringIO() as display, redirect_stdout(display):
            Rectangle(2, 3, 2, 3).display()
            r = display.getvalue()
        self.assertEqual(r, "\n\n\n  ##\n  ##\n  ##\n")

    def test_str(self):
        """tests the str method"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")

    def test_update(self):
        """tests the update method"""
        r1 = Rectangle(10, 10, 10, 10, 1)
        self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 10/10")
        r1.update(89)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 10/10")
        r1.update(89, 2)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/10")
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/5 - 2/3")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1.update(89, 2, "3", 4, 5)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r1.update(89, 2, 3, -4, 5)

    def test_updateargs(self):
        """tests the update with args and kwargs"""
        r1 = Rectangle(10, 10, 10, 10, 1)
        r1.update(width=1, x=2)
        self.assertEqual(str(r1), "[Rectangle] (1) 2/10 - 1/10")
        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r1), "[Rectangle] (89) 3/1 - 2/10")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1.update(height="3")
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r1.update(x=-3)

    def test_to_dictionary(self):
        """tests the dictionary method"""
        r1 = Rectangle(10, 2, 1, 9, 89)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle(1, 1)
        s = "{'id': 89, 'width': 10, 'height': 2, 'x': 1, 'y': 9}"
        self.assertEqual(str(r1_dictionary), s)
        r2.update(**r1_dictionary)
        self.assertEqual(str(r2), "[Rectangle] (89) 1/9 - 10/2")

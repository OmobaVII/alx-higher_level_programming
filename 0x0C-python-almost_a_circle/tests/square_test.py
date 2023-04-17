#!/usr/bin/python3
"""
Unittest for Square
"""


import os
import unittest
from io import StringIO
from contextlib import redirect_stdout
from models import rectangle
from models import square
Square = square.Square


class TestSquare(unittest.TestCase):
    """test for the class Square"""

    def test_attributes(self): 

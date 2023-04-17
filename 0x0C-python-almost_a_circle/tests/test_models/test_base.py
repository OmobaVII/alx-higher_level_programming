#!/usr/bin/python3
"""
this is the Unittest for the class Base
"""
import pep8
import csv
import os
import unittest
import json
from models import base
from models import rectangle
from models import square
Base = base.Base
Rectangle = rectangle.Rectangle
Square = square.Square


class Testpep8(unittest.TestCase):
    """tests pep8"""
    def test_Base_pep8(self):
        """pep8 test"""
        style = pep8.StyleGuide(quiet=False)
        file = ["models/base.py", "tests/test_models/test_base.py"]
        err = 0
        err += style.check_files(file).total_errors
        self.assertEqual(err, 0, "Need to fix Pep8")


class TestBase(unittest.TestCase):
    """tests for the Base Class"""

    def setUp(self):
        pass

    def tearDown(self):
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass

    def test_id(self):
        """test of the id"""
        self.assertTrue(Base(23), self.id == 23)
        self.assertTrue(Base(-29), self.id == -29)
        self.assertTrue(Base(752), self.id == 752)
        self.assertTrue(Base(0), self.id == 0)

    def test_toomany_arguments(self):
        """test for too many arguments"""
        with self.assertRaises(TypeError):
            Base(3, 5)
            Base(4, 6, 29)

    def test_increment_id(self):
        """test if the id increments"""
        self.assertTrue(Base(), self.id == 1)
        self.assertTrue(Base(), self.id == 2)
        self.assertTrue(Base(), self.id == 3)

    def test_private(self):
        """Test if private attribute is accesible"""
        with self.assertRaises(AttributeError):
            print(Base.nb_objects)
            print(Base.__nb_objects)

    def test_Base(self):
        """Test if the class is created"""
        self.assertEqual(type(Base(4)), Base)

    def test_to_json_string(self):
        """test if it converts json to string"""
        dict1 = {"id": 5, "width": 3, "height": 5, "x": 1, "y": 3}
        dict2 = {"id": 2, "width": 3, "height": 6, "x": 2, "y": 1}
        rdstr = Base.to_json_string([dict1, dict2])
        self.assertTrue(type(rdstr) == str)
        self.assertTrue(rdstr,
                        [{"id": 5, "width": 3, "height": 5, "x": 1, "y": 3},
                         {"id": 2, "width": 3, "height": 6, "x": 2, "y": 1}])
        self.assertTrue(type(dict1) == dict)
        dict3 = None
        rdstr1 = Base.to_json_string([dict3])
        self.assertTrue(rdstr1, "[]")
        self.assertTrue(type(rdstr1) == str)
        dict4 = dict()
        rdstr2 = Base.to_json_string([dict4])
        self.assertTrue(type(rdstr2) == str)
        self.assertTrue(rdstr2, "[]")
        self.assertTrue(type(dict4) == dict)

    def test_save_to_file(self):
        """Test for the save_to_file"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as myFile:
            self.assertEqual(json.dumps([r1.to_dictionary(),
                                        r2.to_dictionary()]),
                             myFile.read())

    def test_save_to_file2(self):
        """test the save_to_file with none and empty"""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as myFile:
            self.assertTrue('[]', myFile.read())

        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as myFile:
            self.assertTrue('[]', myFile.read())

    def test_from_json_string(self):
        """Test for the from_json_string"""
        jstr = '[{"id": 5, "width": 3, "height": 5, "x": 1, "y": 3},\
                 {"id": 2, "width": 3, "height": 6, "x": 2, "y": 1}]'
        str1 = Base.from_json_string(jstr)
        self.assertEqual(str1,
                         [{"id": 5, "width": 3, "height": 5, "x": 1, "y": 3},
                          {"id": 2, "width": 3, "height": 6, "x": 2, "y": 1}])
        self.assertEqual(str1[0],
                         {"id": 5, "width": 3, "height": 5, "x": 1, "y": 3})
        self.assertTrue(type(jstr) == str)
        self.assertTrue(type(str1) == list)
        self.assertTrue(type(str1[0]) == dict)

    def test_from_json_string2(self):
        """test the from_json_string with None and empty"""
        jstr1 = None
        str2 = Base.from_json_string(jstr1)
        self.assertEqual(str2, [])
        self.assertTrue(type(str2) == list)
        jstr2 = ""
        str3 = Base.from_json_string(jstr2)
        self.assertEqual(str3, [])
        self.assertTrue(type(str3) == list)

    def test_create(self):
        """test the create function"""
        rec = Rectangle(3, 5, 1)
        R1 = rec.to_dictionary()
        r2 = Rectangle.create(**R1)
        self.assertEqual(str(r2), "[Rectangle] (1) 1/0 - 3/5")
        self.assertEqual(str(rec), "[Rectangle] (1) 1/0 - 3/5")
        self.assertNotEqual(rec, r2)

    def test_load_from_file(self):
        """test the load from file"""
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]
        Square.save_to_file(list_squares_input)
        s4 = Square.load_from_file()
        self.assertEqual(len(s4), 2)
        for square, num in enumerate(s4):
            if num == 0:
                self.assertEqual(str(square), "[Square] (5) 0/0 - 5")
            if num == 1:
                self.assertEqual(str(square), "[Square] (6) 9/1 - 7")

    def test_load_from_file2(self):
        """test for none and empty"""
        Square.save_to_file(None)
        s4 = Square.load_from_file()
        self.assertEqual(s4, [])
        self.assertEqual(len(s4), 0)
        self.assertTrue(type(s4) == list)

        Square.save_to_file([])
        s5 = Square.load_from_file()
        self.assertEqual(s5, [])
        self.assertEqual(len(s5), 0)
        self.assertTrue(type(s4) == list)

#!/usr/bin/python3
''' Test suite for the console'''


import sys
import models
import unittest
from io import StringIO
from console import HBNBCommand
from unittest.mock import create_autospec


class test_console(unittest.TestCase):
    ''' Test the console module'''
    def setUp(self):
        '''setup for'''
        self.backup = sys.stdout
        self.capt_out = StringIO()
        sys.stdout = self.capt_out

    def tearDown(self):
        ''''''
        sys.stdout = self.backup

    def create(self):
        ''' create an instance of the HBNBCommand class'''
        return HBNBCommand() 

    def test_quit(self):
        ''' Test quit exists'''
        console = self.create()
        self.assertTrue(console.onecmd("quit"))

    def test_EOF(self):
        ''' Test EOF exists'''
        console = self.create()
        self.assertTrue(console.onecmd("EOF"))

    def test_all(self):
        ''' Test all exists'''
        console = self.create()
        console.onecmd("all")
        self.assertTrue(str is type(self.capt_out.getvalue()))

    def test_show(self):
        console = self.create()
        console.onecmd("create User")
        user_id = self.capt_out.getvalue()
        console.onecmd("show User " + user_id)
        x = (self.capt_out.getvalue())
        sys.stdout = self.backup
        print(x)

    '''
    def test_create(self):
        console = self.create()
        self.assertTrue(console.onecmd("create"))

    def test_destroy(self):
        console = self.create()
        self.assertTrue(console.onecmd("destroy"))

    def test_update(self):
        console = self.create()
        self.assertTrue(console.onecmd("update"))

    '''

#!/usr/bin/python3

'''
    All the test for the user model are implemented here.
'''

import os
import pep8
import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    '''
        Testing Review class
    '''

    def test_Review_inheritance(self):
        '''
            tests that the Review class Inherits from BaseModel
        '''
        new_review = Review()
        self.assertIsInstance(new_review, BaseModel)

    def test_Review_attributes(self):
        '''
            Test that Review class has place_id, user_id and text
            attributes.
        '''
        new_review = Review()
        self.assertTrue("place_id" in new_review.__dir__())
        self.assertTrue("user_id" in new_review.__dir__())
        self.assertTrue("text" in new_review.__dir__())

    def test_Review_attributes(self):
        '''
            Test that Review class has place_id, user_id and text
            attributes.
        '''
        new_review = Review()
        place_id = getattr(new_review, "place_id")
        user_id = getattr(new_review, "user_id")
        text = getattr(new_review, "text")
        self.assertIsInstance(place_id, str)
        self.assertIsInstance(user_id, str)
        self.assertIsInstance(text, str)

    def test_is_subclass(self):
        self.assertTrue(issubclass(self.rev1.__class__, BaseModel), True)

    def test_checking_for_functions(self):
        self.assertIsNotNone(Review.__doc__)

    def test_has_attributes(self):
        self.assertTrue('id' in self.rev1.__dict__)
        self.assertTrue('created_at' in self.rev1.__dict__)
        self.assertTrue('updated_at' in self.rev1.__dict__)
        self.assertTrue('place_id' in self.rev1.__dict__)
        self.assertTrue('text' in self.rev1.__dict__)
        self.assertTrue('user_id' in self.rev1.__dict__)

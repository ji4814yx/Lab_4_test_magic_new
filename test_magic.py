""" TODO create a test case to test each of the following functions,

generate_url_for_question
 - check that the expected URL is returned for an example question. 

extract_answer_from_response
 - one test should create some example dictionaries that match the expected response from the API,
 and check that the correct answer is extracted and returned.
 - another test should create example dictionaries with a different structure to the one returned from the API, 
 and check that the function returns None. 

 
 TODO to think about - what else could you test about this program? 
 What types of expected and unexpected behavior might happen? You may be able to write tests for some 
 of your ideas now. We'll talk about ways to test other aspects of this program in class.

"""
from unittest import TestCase
import json
import functions_magic
import nturl2path


class GenerateUrlForQuestionTest(TestCase):

    def test_generate_url_for_question(self):  # I watch this unit testing from
        # https://www.youtube.com/watch?v=HKTyOUx9Wf4
        pass


class ExtractAnswerFromResponse(TestCase):

    def test_extrac_answer_from_response(self):
        pass

# I can also test the following functions:
# def make_request_to_magic_8_ball(url):
# and
# def extract_answer_from_response(response):

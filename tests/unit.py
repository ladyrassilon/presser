import unittest
import responses
import requests

from mock import patch

from presser.presser import Presser
from presser.exceptions import Presser404Error, PresserURLError, PresserInvalidVineIdError

VINE_URL = 'https://vine.co/v/M0WmADraAD2'
VINE_ID = 'M0WmADraAD2'

NOT_FOUND_URL = "https://vine.co/v/NOTAVINE"

class PressingUnitTest(unittest.TestCase):

    def setUp(self):
        self.presser = Presser()

    def test_not_vine_url(self):
        self.assertRaises(PresserURLError, self.presser.get_data_for_vine_from_url, "http://www.google.com")

    def test_not_a_valid_vine_id(self):
        non_word_url = "https://vine.co/v/{}".format("!@#$%^")
        self.assertRaises(PresserInvalidVineIdError, self.presser.get_data_for_vine_from_url, non_word_url)

    @patch('presser.presser.Presser.get_data_for_vine_id')
    def test_vine_id_extraction(self, vine_response):
        vine = self.presser.get_data_for_vine_from_url(VINE_URL)
        self.presser.get_data_for_vine_id.assert_called_with(VINE_ID)

    @responses.activate
    def test_vine_data_extraction(self):
        with open("tests/dummy.html") as dummy_html:
            body = dummy_html.read()
        responses.add(responses.GET, VINE_URL,
                  body=body, status=200,
                  content_type='text/html')
        vine = self.presser.get_data_for_vine_id(VINE_ID)
        self.assertEqual(VINE_URL, vine["permalinkUrl"])

    @responses.activate
    def test_404_detection_logic(self):
        with open("tests/404.html") as not_found_html:
            body = not_found_html.read()
        responses.add(responses.GET, NOT_FOUND_URL,
                    body=body, status=200,
                    content_type='text/html')
        self.assertRaises(Presser404Error, self.presser.get_data_for_vine_from_url, "https://vine.co/v/NOTAVINE")

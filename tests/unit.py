import unittest
import responses
import requests

from mock import patch

from presser.presser import Presser
from presser.exceptions import Presser404Error, PresserURLError, PresserInvalidVineIdError, PresserJavaScriptParseError, PresserRequestError

VINE_URL = 'https://vine.co/v/M0WmADraAD2'
VINE_ID = 'M0WmADraAD2'

NOT_FOUND_URL = "https://vine.co/v/NOTAVINE"

def dummy_error_get(*args, **kwargs):
    raise requests.exceptions.RequestException("Dummy Error")

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
        self.assertRaises(Presser404Error, self.presser.get_data_for_vine_from_url, NOT_FOUND_URL)

    @responses.activate
    def test_no_script_in_valid_vine_page(self):
        with open("tests/no_script.html") as no_script:
            body = no_script.read()
        responses.add(responses.GET, VINE_URL,
                    body=body, status=200,
                    content_type='text/html')
        self.assertRaises(PresserJavaScriptParseError, self.presser.get_data_for_vine_from_url, VINE_URL)

    @responses.activate
    def test_extra_script_in_valid_vine_page(self):
        with open("tests/extra_script_tag.html") as extra_script_tag:
            body = extra_script_tag.read()
        responses.add(responses.GET, VINE_URL,
                    body=body, status=200,
                    content_type='text/html')
        self.assertRaises(PresserJavaScriptParseError, self.presser.get_data_for_vine_from_url, VINE_URL)

    @responses.activate
    def test_extra_script_in_valid_vine_page(self):
        with open("tests/broken_js.html") as broken_js:
            body = broken_js.read()
        responses.add(responses.GET, VINE_URL,
                    body=body, status=200,
                    content_type='text/html')
        self.assertRaises(PresserJavaScriptParseError, self.presser.get_data_for_vine_from_url, VINE_URL)

    @patch("requests.get", dummy_error_get)
    def test_error_request(self):
        self.assertRaises(PresserRequestError, self.presser.get_data_for_vine_from_url, VINE_URL)

    @patch("requests.models.Response.ok", False)
    def test_page_not_okay(self):
        self.assertRaises(PresserURLError, self.presser.get_data_for_vine_from_url, VINE_URL)
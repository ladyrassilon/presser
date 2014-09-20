import unittest
import responses
import requests

from mock import patch

from presser.presser import Presser
from presser.exceptions import PresserJavaScriptParseError, PresserURLError

VINE_URL = 'https://vine.co/v/M0WmADraAD2'
VINE_ID = 'M0WmADraAD2'

class PressingUnitTest(unittest.TestCase):

    def setUp(self):
        self.presser = Presser()

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
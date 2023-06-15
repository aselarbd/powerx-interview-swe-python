import unittest
from main import app
from flask.testing import FlaskClient


class AddDataTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.client: FlaskClient = app.test_client()

    def test_add_data_success(self):
        # Prepare the data for the POST request
        data = '1649941817 Voltage 1.34\n1649941818 Voltage 1.35\n1649941817 Current 12.0'

        # Send the POST request with the appropriate content type
        response = self.client.post('/data', data=data, content_type='text/plain')

        # Assert the response
        self.assertEqual(response.status_code, 201)
        response_data = response.get_json()
        self.assertEqual(response_data['success'], True)

    def test_add_data_failure(self):
        # Prepare the data for the POST request
        data = '1649941817 Voltage 1.34\n1649941818 Voltage 1.35\n1649941817 12.0 Current'

        # Send the POST request with the appropriate content type
        response = self.client.post('/data', data=data, content_type='text/plain')

        # Assert the response
        self.assertEqual(response.status_code, 400)
        response_data = response.get_json()
        self.assertEqual(response_data['success'], False)

    # TODO: Add more unit tests for validator functions and service function

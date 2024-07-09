import unittest
from unittest.mock import patch

import httpx

from api.api import get_characters
from api.api import get_location


class TestAPI(unittest.TestCase):
    @patch("api.api.httpx.get")
    def test_get_characters(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "results": [{"name": "Rick Sanchez"}],
            "info": {"next": "some_url"},
        }

        response = get_characters(1)
        self.assertIn("results", response)
        self.assertIn("info", response)

    @patch("api.api.random.choice", return_value=True)
    @patch("api.api.time.sleep", return_value=None)
    @patch("api.api.httpx.get")
    def test_get_location_timeout(self, mock_get, mock_sleep, mock_choice):
        with self.assertRaises(httpx.TimeoutException):
            get_location("some_url")

    @patch("api.api.random.choice", return_value=False)
    @patch("api.api.httpx.get")
    def test_get_location(self, mock_get, mock_choice):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"name": "Earth"}

        response = get_location("some_url")
        self.assertIn("name", response)


if __name__ == "__main__":
    unittest.main()

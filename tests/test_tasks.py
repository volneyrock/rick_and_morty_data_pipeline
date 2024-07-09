import json
import unittest
from unittest.mock import patch

import httpx
from prefect.exceptions import FailedRun

from tasks.prefect_tasks import fetch_character_location
from tasks.prefect_tasks import fetch_characters
from tasks.prefect_tasks import save_to_json


class TestTasks(unittest.TestCase):
    @patch("tasks.prefect_tasks.get_characters")
    def test_fetch_characters(self, mock_get_characters):
        mock_get_characters.side_effect = [
            {
                "results": [{"name": "Rick Sanchez"}],
                "info": {"next": "some_url"},
            },
            {"results": [{"name": "Morty Smith"}], "info": {"next": None}},
        ]

        characters = fetch_characters.fn(max_pages=2)
        self.assertEqual(len(characters), 2)
        self.assertEqual(characters[0]["name"], "Rick Sanchez")
        self.assertEqual(characters[1]["name"], "Morty Smith")

    @patch("tasks.prefect_tasks.get_location")
    def test_fetch_location_for_character(self, mock_get_location):
        mock_get_location.return_value = {"name": "Earth"}

        character = {"name": "Rick Sanchez", "location": {"url": "some_url"}}
        result = fetch_character_location.fn(character)
        self.assertEqual(result["character"], "Rick Sanchez")
        self.assertEqual(result["location"], "Earth")

    @patch(
        "tasks.prefect_tasks.get_location", side_effect=httpx.TimeoutException
    )
    def test_fetch_location_for_character_timeout(self, mock_get_location):
        character = {"name": "Rick Sanchez", "location": {"url": "some_url"}}
        with self.assertRaises(FailedRun):
            fetch_character_location.fn(character)

    def test_save_data_to_json(self):
        data = [{"character": "Rick Sanchez", "location": "Earth"}]
        save_to_json.fn(data, "test.json")
        with open("test.json", "r") as f:
            content = json.load(f)
        self.assertEqual(content, data)


if __name__ == "__main__":
    unittest.main()

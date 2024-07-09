import json

from prefect import get_run_logger
from prefect import task
from prefect.exceptions import FailedRun

from api.api import get_characters
from api.api import get_location


@task
def fetch_characters(max_pages: int = 1) -> list:
    characters = []
    page = 1
    while page <= max_pages:
        try:
            response = get_characters(page)
            characters.extend(response["results"])
            if response["info"]["next"]:
                page += 1
            else:
                break
        except Exception as e:
            raise FailedRun(f"Failed to fetch characters: {str(e)}")
    return characters


@task
def fetch_character_location(character: dict) -> dict:
    try:
        location_url = character["location"]["url"]
        if location_url:
            location = get_location(location_url)
            return {
                "character": character["name"],
                "location": location["name"],
            }
        else:
            return {"character": character["name"], "location": "Unknown"}
    except Exception as e:
        raise FailedRun(
            f"Failed to fetch location for character {character['name']}: {str(e)}"  # noqa E501
        )


@task
def save_to_json(data, filename):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
    logger = get_run_logger()
    logger.info(f"Data saved to {filename}")

from prefect import flow

from tasks.prefect_tasks import fetch_character_location
from tasks.prefect_tasks import fetch_characters
from tasks.prefect_tasks import save_to_json


@flow(
    name="Rick and Morty Flow",
    log_prints=True,
    retry_delay_seconds=10,
    retries=8,
)
def rick_and_morty_flow(max_pages: int = 1):
    characters = fetch_characters(max_pages)
    character_locations = fetch_character_location.map(characters)
    save_to_json(character_locations, "rick_and_morty.json")


if __name__ == "__main__":
    rick_and_morty_flow()

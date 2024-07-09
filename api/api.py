import random
import time
import httpx


BASE_URL = "https://rickandmortyapi.com/api"


def get_characters(page: int = 1) -> dict:
    url = f"{BASE_URL}/character/?page={page}"
    response = httpx.get(url)
    response.raise_for_status()
    return response.json()


def get_location(url: str) -> dict:
    # Simulando timeout
    if random.choice([True, False]):
        time.sleep(5)
        raise httpx.TimeoutException("Timeout simulated")
    response = httpx.get(url)
    response.raise_for_status()
    return response.json()
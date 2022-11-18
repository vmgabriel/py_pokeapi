"""Request PokeAPI Adapter"""

# Libraries
from functools import lru_cache
from requests import post


class Request:
    url: str

    def __init__(self, url: str):
        self.url = url

    @lru_cache
    def send(self, query: str) -> dict:
        r = post(self.url, json={"query": query})
        return r.json()

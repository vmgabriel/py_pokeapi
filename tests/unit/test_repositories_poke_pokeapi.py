# Libraries
import unittest
from unittest.mock import MagicMock
from requests.exceptions import RequestException

# modules
from adapters.repositories.poke.pokeapi import pokeapi, request


class TestPokeAPI(unittest.TestCase):
    def setUp(self) -> None:
        self.berry_test = [
            {"id": 1, "name": "a_name", "growth_time": 3},
            {"id": 2, "name": "b_name", "growth_time": 4},
            {"id": 3, "name": "c_name", "growth_time": 5},
            {"id": 4, "name": "d_name", "growth_time": 5},
        ]

    def test_get_berries_ok(self):
        request_mock = request.Request("url")
        request_mock.send = MagicMock()
        request_mock.send.return_value = {"data": {"pokemon_v2_berry": self.berry_test}}

        self.poke = pokeapi.PyPokeAPIPokeRepository(request_mock)
        berries = self.poke.get_berries()

        request_mock.send.assert_called_once()
        assert len(berries) == len(self.berry_test)
        assert [x.name for x in berries] == [x["name"] for x in self.berry_test]

    def test_get_berries_error(self):
        error_str = "Error Request"
        request_mock = request.Request("url")
        request_mock.send = MagicMock()
        request_mock.send.side_effect = RequestException(error_str)

        self.poke = pokeapi.PyPokeAPIPokeRepository(request_mock)
        berries = self.poke.get_berries()

        request_mock.send.assert_called_once()
        assert berries == []

    def test_get_berries_incorrect_struct(self):
        error_str = "Error Request"
        request_mock = request.Request("url")
        request_mock.send = MagicMock()
        request_mock.send.return_value = {"a": "worse_structure"}

        self.poke = pokeapi.PyPokeAPIPokeRepository(request_mock)
        berries = self.poke.get_berries()

        request_mock.send.assert_called_once()
        assert berries == []

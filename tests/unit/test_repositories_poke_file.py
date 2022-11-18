# Libraries
import unittest
from unittest.mock import Mock

# Modules
from adapters.repositories.poke.file import file, reader


class TestFile(unittest.TestCase):
    def setUp(self):
        self.berry_data = reader.CsvData(headers=["id", "name", "growth_time", "url"], contents=[
            ["1", "a_name", "2", "url"],
            ["2", "b_name", "3", "url"],
            ["3", "b_name", "4", "url"],
            ["4", "b_name", "5", "url"],
        ])
        self.poke = file.FilePokeRepository()

    def test_get_berries_ok(self):
        file.reader.read_fixture = Mock(return_value=self.berry_data)

        berries = self.poke.get_berries()
        file.reader.read_fixture.assert_called_once()
        assert len(berries) == len(self.berry_data.contents)
        assert [x.name for x in berries] == [x[1] for x in self.berry_data.contents]

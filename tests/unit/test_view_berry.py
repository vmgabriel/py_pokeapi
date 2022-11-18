# Libraries
import unittest
from unittest.mock import Mock

# Modules
import messages
from domain import models, factories, repositories
from views.berry import berry_view, BerryStatistics


class PokeDummyRepository(repositories.PokeRepository):
    def get_berries(self) -> list[models.Berry]:
        return []


class BerryViewCase(unittest.TestCase):
    def setUp(self) -> None:
        self.berry_test = [
            models.Berry(1, "a_name", 3, ""),
            models.Berry(2, "b_name", 4, ""),
            models.Berry(3, "c_name", 5, ""),
            models.Berry(3, "d_name", 6, ""),
        ]


    def test_struct(self):
        berry = models.Berry(1,"a_name", 3, "")
        assert berry.name == berry_view._struct(berry)

    def test_statistics(self):
        should_be = BerryStatistics(
            median=4.5,
            min=3,
            max=6,
            variance=1.6666666666666667,
            mean=4.5,
            frequency=3,
            frequency_absolute={3: 1, 4: 1, 5: 1, 6: 1},
        )
        assert berry_view._statistics(self.berry_test, "growth_time") == should_be

    def test_list(self):
        poke_repository = PokeDummyRepository()
        poke_repository.get_berries = Mock(return_value=self.berry_test)
        factory_mock = factories.Server(poke_repository)
        message_test = messages.PokeApiResponse(
            berries_names=["a_name", "b_name", "c_name", "d_name"],
            min_growth_time=3,
            median_growth_time=4.5,
            max_growth_time=6,
            variance_growth_time=1.6666666666666667,
            mean_growth_time=4.5,
            frequency_growth_time=3,
            absolute_frequencies_growth_time={3: 1, 4: 1, 5: 1, 6: 1},
        )
        data_listed = berry_view.list(factory_mock)
        assert data_listed == message_test


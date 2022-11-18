# Libraries
import unittest
from unittest.mock import MagicMock

# Modules
from domain import factories, repositories, models


class PokeDummyRepository(repositories.PokeRepository):
    def get_berries(self) -> list[models.Berry]:
        return []


class FactoryServiceCase(unittest.TestCase):
    def setUp(self) -> None:
        self.poke_repository = PokeDummyRepository
        self.factory_server = factories.ServerFactory(
            poke_repository=self.poke_repository
        )

    def test_generate_a_new_service(self):
        server = self.factory_server()
        assert server.poke_repository.__class__ == self.poke_repository


if __name__ == '__main__':
    unittest.main()

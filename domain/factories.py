"""Factories Domain"""

# Libraries
from abc import ABC, abstractmethod
from dataclasses import dataclass

# Modules
from domain import repositories


@dataclass
class Server:
    poke_repository: repositories.PokeRepository


class ServerFactory(ABC):
    """Server Factory"""
    poke_repository: type(repositories.PokeRepository)

    def __init__(
            self,
            poke_repository: type(repositories.PokeRepository)
    ):
        self.poke_repository = poke_repository

    def __call__(self):
        return Server(
            poke_repository=self.poke_repository()
        )

"""Repositories Domain"""

# Libraries
from abc import ABC, abstractmethod

# Modules
from domain import models


class PokeRepository(ABC):
    @abstractmethod
    def get_berries(self) -> list[models.Berry]:
        raise NotImplementedError()

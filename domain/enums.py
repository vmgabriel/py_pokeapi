"""Domain Enums"""

# Libraries
from enum import Enum


class Environment(str, Enum):
    dev = "dev"
    qa = "qa"
    prod = "prod"


class PokeRepository(str, Enum):
    file = "file"  # use file
    pokeapi = "pokeapi"  # use Pokeapi repository

"""Repositories Poke Adapter"""

# Modules
from config import config
from domain import enums, repositories
from . import file, pokeapi

# To Select Modules
poke_modules: dict[enums.PokeRepository, type(repositories.PokeRepository)] = {
    enums.PokeRepository.file: file.FilePokeRepository,
    enums.PokeRepository.pokeapi: pokeapi.PyPokeAPIPokeRepository,
}


# Modules
poke_module: repositories.PokeRepository = poke_modules[config.POKEMON_REPOSITORY]

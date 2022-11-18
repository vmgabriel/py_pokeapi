"""Config Main"""

# Libraries
from os import getenv
from pathlib import Path
from dotenv import load_dotenv
from logging import getLogger

# Modules
from domain import enums


# Base Config
main_path = Path()
env_path = main_path / ".env"
load_dotenv(env_path)


environment = enums.Environment(getenv("ENV", "dev").lower())


class Config:
    MODULE_NAME: str = "pokeapi"
    DEBUG: bool = False
    APPLICATION_VERSION = "1.0.0"
    ROOT_PATH: Path = main_path
    PORT: int = int(getenv("PORT", "8000"))

    ENV: enums.Environment = environment
    POKEMON_REPOSITORY = enums.PokeRepository("file")

    CORS_ALLOWED_ORIGINS = [
        "*"
    ]


class DevConfig(Config):
    DEBUG = True


class QAConfig(Config):
    POKEMON_REPOSITORY = enums.PokeRepository("pokeapi")


class ProdConfig(Config):
    POKEMON_REPOSITORY = enums.PokeRepository("pokeapi")


match_environment: dict[enums.Environment, type(Config)] = {
    enums.Environment.dev: DevConfig,
    enums.Environment.qa: QAConfig,
    enums.Environment.prod: ProdConfig,
}


config: Config = match_environment[environment]()
logger = getLogger(config.MODULE_NAME)

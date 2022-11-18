"""File Repository Adapter"""

# Libraries
from pathlib import Path

# Modules
from domain import repositories, models
from config import config
from . import reader


class FilePokeRepository(repositories.PokeRepository):
    structure: str
    content: Path

    def __init__(self):
        self.structure = "int,str,int,str"
        self.content = config.ROOT_PATH / "db.csv"

    def get_berries(self) -> list[models.Berry]:
        contents: reader.CsvData = reader.define_structure(
            reader.read_fixture(self.content.absolute()),
            self.structure,
        )
        return [models.Berry(*x) for x in contents.contents]
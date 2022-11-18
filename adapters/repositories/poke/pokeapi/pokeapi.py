"""Adapter Repository PokeAPI"""

# Modules
from domain import repositories, models
from config import logger
from .request import Request


class PyPokeAPIPokeRepository(repositories.PokeRepository):
    url: str
    request: Request

    def __init__(self, request: Request = None):
        self.url = "https://beta.pokeapi.co/graphql/v1beta"
        self.request = request or Request(self.url)

    def get_berries(self) -> list[models.Berry]:
        query = "query samplePokeAPIquery { pokemon_v2_berry { id, name, growth_time, }}"
        try:
            data = self.request.send(query)
            if not ("data" in data and "pokemon_v2_berry" in data["data"]):
                raise Exception("Error Struct of Endpoint Modified")
            datas: list[dict] = data["data"]["pokemon_v2_berry"]
            return [models.Berry(id=dt["id"], name=dt["name"], growth_time=dt["growth_time"], url="") for dt in datas]
        except Exception as exc:
            logger.error(f"[Error][PokeAPI] - {repr(exc)}")
        return []

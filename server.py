"""Unit of Work"""

# Modules
from domain import factories
from adapters.repositories import poke_repository


class ServerFastApiFactory(factories.ServerFactory):
    def __init__(self):
        super().__init__(poke_repository)


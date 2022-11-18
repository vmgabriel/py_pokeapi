"""All Messages Entrypoints"""

# Libraries
from pydantic import BaseModel


class PokeApiResponse(BaseModel):
    """PokeApi Response Content"""
    berries_names: list[str]
    min_growth_time: int
    median_growth_time: float
    max_growth_time: int
    variance_growth_time: float
    mean_growth_time: float
    frequency_growth_time: float
    absolute_frequencies_growth_time: dict[str, int]

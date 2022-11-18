"""Model Domain"""

# Libraries
from dataclasses import dataclass


@dataclass
class Berry:
    id: int
    name: str
    growth_time: int
    url: str

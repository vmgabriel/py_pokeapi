"""Berry View"""

# Libraries
from itertools import groupby
from dataclasses import dataclass
import statistics

# Modules
import messages
from domain import factories, models


@dataclass
class BerryStatistics:
    median: float
    min: float
    max: float
    variance: float
    mean: float
    frequency: float
    frequency_absolute: dict[int, int]


class BerryView:
    def _struct(self, berry: models.Berry):
        return berry.name

    def _statistics(self, berries: list[models.Berry], attribute: str) -> BerryStatistics:
        data: list[int] = [getattr(berry, attribute) for berry in berries]
        return BerryStatistics(
            median=statistics.median(data),
            min=min(data),
            max=max(data),
            variance=statistics.variance(data),
            mean=statistics.mean(data),
            frequency=statistics.mode(data),
            frequency_absolute={x: len(list(y)) for x, y in groupby(data)},
        )

    def list(self, uow: factories.Server) -> messages.PokeApiResponse:
        berries = uow.poke_repository.get_berries()
        stc = self._statistics(berries, attribute="growth_time")
        return messages.PokeApiResponse(
            berries_names=[self._struct(berry) for berry in berries],
            min_growth_time=stc.min,
            median_growth_time=stc.median,
            max_growth_time=stc.max,
            variance_growth_time=stc.variance,
            mean_growth_time=stc.mean,
            frequency_growth_time=stc.frequency,
            absolute_frequencies_growth_time=stc.frequency_absolute,
        )


berry_view = BerryView()

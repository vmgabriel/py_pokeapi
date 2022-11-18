"""Berry Matplot"""

# Libraries
import altair as alt
from domain import factories
from .berry import berry_view


class Content:
    content = None

    def write(self, content):
        self.content = content


def html(uow: factories.Server) -> str:
    berries = berry_view.list(uow)
    data = alt.Data(values=[
        {"growth_time": x, "quantiy": y} for x, y in berries.absolute_frequencies_growth_time.items()
    ])

    chart = alt.Chart(
        data,
        title="Poke-API Berries growth_time Absolute Frequency"
    ).mark_bar().encode(
        alt.X("growth_time:O", bin=True),
        y='quantiy:Q',
    )
    x = Content()
    chart.save(x, format="html")
    return x.content

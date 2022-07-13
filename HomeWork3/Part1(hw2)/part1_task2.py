from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Generator, List, Tuple


@dataclass
class Movie:
    title: str
    dates: List[Tuple[datetime, datetime]]

    def schedule(self) -> Generator[datetime, None, None]:
        for date in self.dates:
            num_days = (date[1] - date[0]).days
            date_list = [date[0] + timedelta(days=x) for x in range(num_days + 1)]
            for day in date_list:
                yield day


m = Movie('sw', [
  (datetime(2020, 1, 1), datetime(2020, 1, 7)),
  (datetime(2020, 1, 15), datetime(2020, 2, 7)),
])

for d in m.schedule():
    print(d)

from dataclasses import dataclass, field
from typing import List, Optional
from dataclasses_json import dataclass_json

from telewbot.models.basic import Main
from telewbot.models.weather import Weather
from telewbot.models.wind import Wind

@dataclass_json
@dataclass
class WeatherResponse:
    base: str
    cod: int
    dt: int
    id: int
    main: Main
    name: str
    timezone: int
    visibility: int
    weather: List[Weather]
    wind: Wind

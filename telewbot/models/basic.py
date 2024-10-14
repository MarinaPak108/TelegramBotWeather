from dataclasses import dataclass
from typing import Optional
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class Main:
    feels_like: float
    grnd_level: Optional[int]
    humidity: int
    pressure: int
    sea_level: Optional[int]
    temp: float
    temp_max: float
    temp_min: float
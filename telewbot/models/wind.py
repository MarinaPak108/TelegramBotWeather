from dataclasses import dataclass
from typing import Optional
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class Wind:
    speed: float
    deg: int
    gust: Optional[float] = None
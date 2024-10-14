from dataclasses import dataclass
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class Weather:
    id: int
    main: str
    description: str
    icon: str
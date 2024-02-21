from json import JSONEncoder
from dataclasses import is_dataclass, asdict
from typing import Any

class Encoder(JSONEncoder):
    def default(self, o: Any) -> str:
        if is_dataclass(o):
            return asdict(o)
        return super().default(o)

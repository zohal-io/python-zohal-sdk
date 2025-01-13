from dataclasses import dataclass
from typing import Optional

from dataclasses_json import dataclass_json

from . import Gender


@dataclass_json
@dataclass
class NationalIdentity:
    matched: bool
    last_name: str
    first_name: str
    father_name: str
    national_code: str
    is_dead: bool
    alive: bool
    gender: Optional[Gender]

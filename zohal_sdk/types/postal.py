from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class PostalCode:
    province: str
    town: str
    district: str
    street: str
    street2: str
    number: int
    floor: int
    side_floor: int
    building_name: str
    description: str

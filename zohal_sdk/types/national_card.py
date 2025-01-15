from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class NationalCard:
    first_name: str
    last_name: str
    father_name: str
    national_code: str
    birth_date: str
    city: str
    province: str
    face_photo: str

from dataclasses import dataclass
from dataclasses_json import dataclass_json

from ..types import RequestData


@dataclass_json
@dataclass
class CheckCardWithNationalCodeRequest(RequestData):
    national_code: str
    birth_date: str
    card_number: str

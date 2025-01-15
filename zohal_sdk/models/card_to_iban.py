from ..types import RequestData
from dataclasses_json import dataclass_json
from dataclasses import dataclass


@dataclass_json
@dataclass
class CardToIBANRequest(RequestData):
    card_number: str

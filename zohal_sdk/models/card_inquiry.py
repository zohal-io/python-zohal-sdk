from dataclasses import dataclass
from dataclasses_json import dataclass_json
from ..types import RequestData


@dataclass_json
@dataclass
class CardInquiryRequest(RequestData):
    card_number: str

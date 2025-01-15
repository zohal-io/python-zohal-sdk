from dataclasses import dataclass
from dataclasses_json import dataclass_json

from ..types import RequestData


@dataclass_json
@dataclass
class PostalCodeInquiry(RequestData):
    postal_code: str

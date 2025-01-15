from typing import Optional
from dataclasses_json import dataclass_json
from dataclasses import dataclass

from ..types import RequestData


@dataclass_json
@dataclass
class IBANRequest(RequestData):
    iban: str
    separated: Optional[bool]

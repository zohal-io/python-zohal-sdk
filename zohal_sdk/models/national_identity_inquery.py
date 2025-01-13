from typing import Optional

from dataclasses import dataclass
from dataclasses_json import dataclass_json

from ..types import RequestData


@dataclass_json
@dataclass
class NationalIdentityInqueryRequest(RequestData):
    birth_date: str
    national_code: str
    gender: Optional[bool] = None

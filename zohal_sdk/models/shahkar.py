from dataclasses_json import dataclass_json
from dataclasses import dataclass
from ..types import RequestData


@dataclass_json
@dataclass
class ShahkarRequest(RequestData):
    national_code: str
    mobile: str

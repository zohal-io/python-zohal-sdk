from dataclasses import dataclass
from dataclasses_json import dataclass_json
from ..types import RequestData


@dataclass_json
@dataclass
class PersianToFinglishRequest(RequestData):
    persian_text: str

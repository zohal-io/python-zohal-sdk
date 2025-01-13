from typing import Protocol, Optional, runtime_checkable, Any
from enum import Enum

from dataclasses import dataclass
from dataclasses_json import dataclass_json, CatchAll, Undefined


@runtime_checkable
class RequestData(Protocol):
    pass


@runtime_checkable
class BaseResponseData(Protocol):
    pass


@dataclass_json(undefined=Undefined.INCLUDE)
@dataclass
class ResponseBody:
    data: Any
    catch: CatchAll
    message: str
    error_code: Optional[dict]

    def __post_init__(self):
        self.data = self.catch.get("data_type")(**self.data)


@dataclass_json
@dataclass
class ResponseData:
    response_body: ResponseBody
    result: int

    @classmethod
    def serialize(cls, t, data):
        data["response_body"]['data_type'] = t
        return cls.from_dict(data)


class Gender(int, Enum):
    MALE = 1
    FEMALE = 0

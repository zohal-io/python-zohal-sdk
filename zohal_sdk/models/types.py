from typing import Protocol


class RequestData(Protocol):
    pass


class BaseResponseData(Protocol):
    pass


class ResponseData[T](Protocol, BaseResponseData):
    data: T
    message: str

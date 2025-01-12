from requests.exceptions import Timeout
from requests.exceptions import HTTPError as RHTTPError


class TimeoutError(Timeout):
    pass


class HTTPError(RHTTPError):
    pass

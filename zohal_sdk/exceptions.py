from requests.exceptions import Timeout
from requests.exceptions import HTTPError as RHTTPError


class TimeoutError(Timeout):
    """
    Raises when api request has been timeout.
        """
    pass


class HTTPError(RHTTPError):
    """
    Any HTTPError happen during requests gonna be instance of this error.
    """
    pass


class ZohalError(Exception):
    """
    Internal Error or Any Error that came from zohal api.
    """
    pass

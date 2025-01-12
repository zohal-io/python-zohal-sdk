from requests import Session
from requests.exceptions import (Timeout, HTTPError as RHTTPError,
                                 JSONDecodeError)
import logging

from .exceptions import HTTPError, TimeoutError

logger = logging.getLogger(__name__)

BASE_URL = "https://service.zohal.io/api"


class Client:

    def __init__(self, token: str):
        self.token = token
        self.session = Session()
        self.session.headers['Authorization'] = f'Bearer {self.token}'

    def _request(self, url: str, method: str = "GET"):
        logger.debug(f"request to {url=} with {method=}")
        try:
            response = self.session.request(method, url)
            logger.debug(
                f"got response with status code {response.status_code}")
            response.raise_for_status()
            data = response.json()
            return data
        # TODO: change this later
        except RHTTPError as e:
            raise HTTPError from e
        except Timeout as e:
            raise TimeoutError from e
        except JSONDecodeError as e:
            raise e

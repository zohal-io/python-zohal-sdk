from typing import Optional
from dataclasses import asdict
import logging
from requests import Session
from requests.exceptions import (Timeout, HTTPError as RHTTPError,
                                 JSONDecodeError)

from .models import RequestData
from .exceptions import HTTPError, TimeoutError

logger = logging.getLogger(__name__)

BASE_URL = "https://service.zohal.io/api"


class Client:

    def __init__(self, token: str):
        self.token = token
        self.session = Session()
        self.session.headers['Authorization'] = f'Bearer {self.token}'

    def _request(self,
                 url: str,
                 data: Optional[RequestData, dict] = None,
                 method: str = "GET"):
        logger.debug(f"request to {url=} with {method=}")
        try:
            if isinstance(data, RequestData):
                data = asdict(data)
            response = self.session.request(method, url)
            logger.debug(
                f"got response with status code {response.status_code}")
            response.raise_for_status()
            data = response.json()
            return data
        # TODO: change this later
        except RHTTPError as e:
            logger.debug(
                f"raised error status code {e.response.status_code} cause {e.response.text}"
            )
            raise HTTPError from e
        except Timeout as e:
            logger.debug(f"got timeout on {url=} with {method=}")
            raise TimeoutError from e
        except JSONDecodeError as e:
            logger.debug(
                f"raised error while loads json data {e.response.status_code} cause {e.response.text}"
            )
            raise e

""" Zohal RestAPI Client """
from typing import Union
import io
from .types import RequestData
import logging

from requests import Session
from requests.exceptions import (Timeout, HTTPError as RHTTPError,
                                 JSONDecodeError)

from .exceptions import HTTPError, TimeoutError, ZohalError
from .services import InquiryMixin

logger = logging.getLogger(__name__)


class Client(InquiryMixin):

    def __init__(self, token: str):
        if token is None:
            # TODO: Better exception message
            raise ValueError("Token is None")
        self.token = token
        self.session = Session()
        self.session.headers['Authorization'] = f'Bearer {self.token}'

    def request(self,
                url: str,
                data: Union[RequestData, dict, None] = None,
                files=None,
                method: str = "GET"):
        logger.debug(f"request to {url=} with {method=}")
        try:
            kwargs = {"url": url, "method": method}
            if method in ["POST", "PUT", "PATCH"] and isinstance(
                    data, RequestData):
                if data:
                    data = data.to_dict()
                    kwargs['json'] = data

                if files:
                    kwargs['files'] = files

            response = self.session.request(**kwargs)
            logger.debug(
                f"got response with status code {response.status_code}")
            response.raise_for_status()
            data = response.json()
            if data['result'] != 1:
                raise ZohalError(data['response_body']['message'])
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

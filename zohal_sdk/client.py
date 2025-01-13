""" Zohal RestAPI Client """
from typing import Optional, Union
import logging

from requests import Session
from requests.exceptions import (Timeout, HTTPError as RHTTPError,
                                 JSONDecodeError)

from .types import RequestData, ResponseData
from .types.national_identity import NationalIdentity
from .types.shahkar import Shahkar

from .models.shahkar import ShahkarRequest
from .models.national_identity_inquery import NationalIdentityInqueryRequest
from .exceptions import HTTPError, TimeoutError, ZohalError

logger = logging.getLogger(__name__)

BASE_URL = "https://service.zohal.io/api"


class Client:

    def __init__(self, token: str):
        if token is None:
            # TODO: Better exception message
            raise ValueError("Token is None")
        self.token = token
        self.session = Session()
        self.session.headers['Authorization'] = f'Bearer {self.token}'

    def _request(self,
                 url: str,
                 data: Union[RequestData, dict, None] = None,
                 method: str = "GET"):
        logger.debug(f"request to {url=} with {method=}")
        try:
            kwargs = {"url": url, "method": method}
            if method in ["POST", "PUT", "PATCH"] and isinstance(
                    data, RequestData):
                data = data.to_dict()
                kwargs['json'] = data

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

    def national_identity_inquiry(self,
                                  national_code: str,
                                  birth_date: str,
                                  gender: Optional[bool] = None):
        data = NationalIdentityInqueryRequest(national_code=national_code,
                                              birth_date=birth_date,
                                              gender=gender)
        response = self._request(
            f"{BASE_URL}/v0/services/inquiry/national_identity_inquiry",
            data,
            method="POST")
        return ResponseData.serialize(NationalIdentity, response)

    def shahkar(self, national_code: str, mobile: str):
        data = ShahkarRequest(national_code=national_code, mobile=mobile)
        response = self._request(f"{BASE_URL}/v0/services/inquiry/shahkar",
                                 data,
                                 method="POST")
        return ResponseData.serialize(Shahkar, response)

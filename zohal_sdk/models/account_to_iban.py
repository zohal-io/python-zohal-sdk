from dataclasses import dataclass
from dataclasses_json import dataclass_json
from ..types import RequestData
from ..types.bank import BankCode


@dataclass_json
@dataclass
class AccountToIBANRequest(RequestData):
    bank_account: str
    bank_code: BankCode

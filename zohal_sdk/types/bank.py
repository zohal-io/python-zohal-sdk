from typing import Optional
from enum import Enum

from dataclasses import dataclass
from dataclasses_json import dataclass_json


class BankCode(str, Enum):
    Markazi = "010"
    Saman = "056"
    Pasargad = "057"


@dataclass_json
@dataclass
class IBan:
    IBAN: str
    name: Optional[str] = None
    bank_name: Optional[str] = None


@dataclass_json
@dataclass
class BankAccount:
    name: str
    bank_name: str
    bank_account: str


@dataclass_json
@dataclass
class IBANInquiry:
    name: str
    bank_name: str
    is_transferable: bool


@dataclass_json
@dataclass
class Card:
    name: str

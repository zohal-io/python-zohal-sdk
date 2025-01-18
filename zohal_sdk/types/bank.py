from typing import Optional
from enum import Enum

from dataclasses import dataclass
from dataclasses_json import dataclass_json


class BankCode(str, Enum):
    Markazi = "010"
    SanatVaMadan = "011"
    Melat = "012"
    Refah = "013"
    Maskan = "014"
    Sepah = "015"
    Keshavarzi = "016"
    Meli = "017"
    Tejarat = "018"
    Saderat = "019"
    ToseeVaSaderat = "020"
    PostBank = "021"
    ToseVaTaavon = "022"
    MoaseseEtebariTosee = "051"
    Ghavamin = "052"
    KarAfarin = "053"
    Parsian = "054"
    EghtesadNovin = "055"
    Saman = "056"
    Pasargad = "057"
    Sarmaye = "058"
    Sina = "059"
    GharzolhasaneMehr = "060"
    Shahr = "061"
    Ayande = "062"
    Ansar = "063"
    Gardeshgari = "064"
    HekmatIranian = "065"
    Dey = "066"
    IranZamin = "069"
    Resalat = "070"
    MoaseseEtebariKosar = "073"
    MoaseseEtebariMelal = "075"
    Khavarmiyane = "078"
    MehrEghtesad = "079"
    MoaseseEtebariNor = "080"
    IranVenesuela = "095"


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

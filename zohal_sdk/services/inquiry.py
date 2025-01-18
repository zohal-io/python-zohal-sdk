"""InquiryMixin is a mixin for client to add inquiry requests"""

from typing import Optional, Union
import io

from ..types import ResponseData
from ..types.national_identity import NationalIdentity
from ..types.shahkar import Shahkar
from ..types.matched import Matched
from ..types.bank import BankCode, IBan, BankAccount, IBANInquiry, Card
from ..types.finglish import Finglish
from ..types.postal import PostalCode
from ..types.national_card import NationalCard

from ..utils import make_url

from ..models.shahkar import ShahkarRequest
from ..models.national_identity_inquery import NationalIdentityInqueryRequest
from ..models.check_card_with_national_code import CheckCardWithNationalCodeRequest
from ..models.card_to_iban import CardToIBANRequest
from ..models.persian_to_finglish import PersianToFinglishRequest
from ..models.account_to_iban import AccountToIBANRequest
from ..models.card_to_account import CardToAccountRequest
from ..models.iban import IBANRequest
from ..models.card_inquiry import CardInquiryRequest
from ..models.check_card_with_name import CheckCardWithNameRequest
from ..models.check_iban_with_name import CheckIBANWithNameRequest
from ..models.postal_code_inquiry import PostalCodeInquiry


class InquiryMixin:
    service_name = "inquiry"

    def national_identity_inquiry(
            self,
            national_code: str,
            birth_date: str,
            gender: Optional[bool] = None) -> ResponseData[NationalIdentity]:
        """
        National Identity inquiry service
        inquiry national_code with birth_date to see if its valid or not.

        :param national_code: National code
        :param birth_date: birth date in YYYY/MM/DD format
        :param gender: if its true its gonna return gender otherwise it doesnt
        :returns: national identity data
        :rtype: ResponseData<NationalIdentity>
        """
        data = NationalIdentityInqueryRequest(national_code=national_code,
                                              birth_date=birth_date,
                                              gender=gender)
        response = self.request(make_url(self.service_name,
                                         "national_identity_inquiry"),
                                data,
                                method="POST")
        return ResponseData.serialize(NationalIdentity, response)

    def shahkar(self, national_code: str,
                mobile: str) -> ResponseData[Shahkar]:
        """
        Shahkar
        inquiry mobile number with national_code to see if its valid or not.

        :param mobile: mobile number
        :param national_code: national_code
        :returns: true if its matched.
        :rtype: ResponseData<Shahkar>
        """
        data = ShahkarRequest(national_code=national_code, mobile=mobile)
        response = self.request(make_url(self.service_name, "shahkar"),
                                data,
                                method="POST")
        return ResponseData.serialize(Shahkar, response)

    def national_card_ocr(self, national_card_back: Union[io.FileIO, str],
                          national_card_front: Union[io.FileIO, str]):
        """
        National card ocr
        uses OCR on national card to return data of national card and photo of person from national card

        :param national_card_front: front of national card
        :param national_card_back: back of national card
        :returns: National card data.
        :rtype: ResponseData<NationalCard>
        """
        response = self.request(make_url(self.service_name,
                                         "national_card_ocr"),
                                files={
                                    "national_card_back": national_card_back,
                                    "national_card_front": national_card_front,
                                },
                                method="POST")
        return ResponseData.serialize(NationalCard, response)

    def check_card_with_national_code(
            self, national_code: str, birth_date: str,
            card_number: str) -> ResponseData[Matched]:
        """
        Check Card with National Code
        inquiry card number with national code to see if its matches or not

        :param national_code: national code
        :param card_number: card number
        :param birth_date: birth date
        :returns: if matches returns true.
        :rtype: ResponseData<Matched>
        """
        data = CheckCardWithNationalCodeRequest(national_code=national_code,
                                                birth_date=birth_date,
                                                card_number=card_number)
        response = self.request(make_url(self.service_name,
                                         "check_card_with_national_code"),
                                data,
                                method="POST")
        return ResponseData.serialize(Matched, response)

    def card_to_iban(self, card_number: str) -> ResponseData[IBan]:
        """
        Card to IBan
        uses card_number to return IBan

        :param card_number: card number
        :returns: if its successful returns iban.
        :rtype: ResponseData<IBan>
        """
        data = CardToIBANRequest(card_number=card_number)
        response = self.request(make_url(self.service_name, "card_to_iban"),
                                data,
                                method="POST")
        return ResponseData.serialize(IBan, response)

    def card_to_account(self, card_number: str) -> ResponseData[BankAccount]:
        """
        Card to Account
        uses card_number to return account

        :param card_number: card number
        :returns: if its successful returns account.
        :rtype: ResponseData<BankAccount>
        """
        data = CardToAccountRequest(card_number=card_number)
        response = self.request(make_url(self.service_name, "card_to_account"),
                                data,
                                method="POST")
        return ResponseData.serialize(BankAccount, response)

    def iban(self,
             iban: str,
             separated: Optional[bool] = None) -> ResponseData[IBANInquiry]:
        """
        IBan inquiry
        Inquiry to check iban is valid or not

        :param iban: iban
        :param separated: if its true returning name as separated
        :returns: if its successful returns iban.
        :rtype: ResponseData<IBANInquiry>
        """
        data = IBANRequest(iban=iban, separated=separated)
        response = self.request(make_url(self.service_name, "iban"),
                                data,
                                method="POST")
        return ResponseData.serialize(IBANInquiry, response)

    def card_inquiry(self, card_number) -> ResponseData:
        """
        card inquiry
        Inquiry to check card is valid or not

        :param card_number: card number
        :returns: if its successful returns Card.
        :rtype: ResponseData<Card>
        """
        data = CardInquiryRequest(card_number=card_number)
        response = self.request(make_url(self.service_name, "card_inquiry"),
                                data,
                                method="POST")
        return ResponseData.serialize(Card, response)

    def check_card_with_name(self, card_number: str,
                             name: str) -> ResponseData[Matched]:
        """
        check card with name
        Inquiry to check card with name it matches or not

        :param card_number: card number
        :param name: name
        :returns: if it matches returns true.
        :rtype: ResponseData<Matched>
        """
        data = CheckCardWithNameRequest(card_number=card_number, name=name)
        response = self.request(make_url(self.service_name,
                                         "check_card_with_name"),
                                data,
                                method="POST")
        return ResponseData.serialize(Matched, response)

    def check_iban_with_name(self, iban: str,
                             name: str) -> ResponseData[Matched]:
        """
        check iban with name
        Inquiry to check iban with name it matches or not

        :param iban: Iban
        :param name: name
        :returns: if it matches returns true.
        :rtype: ResponseData<Matched>
        """
        data = CheckIBANWithNameRequest(IBAN=iban, name=name)
        response = self.request(make_url(self.service_name,
                                         "check_iban_with_name"),
                                data,
                                method="POST")
        return ResponseData.serialize(Matched, response)

    def postal_code_inquiry(self,
                            postal_code: str) -> ResponseData[PostalCode]:
        """
        postal code inquiry
        Inquiry to retrive postal code data

        :param postal_code: Postal code
        :returns: if its ok returns data of that postal_code.
        :rtype: ResponseData<PostalCode>
        """
        data = PostalCodeInquiry(postal_code=postal_code)
        response = self.request(make_url(self.service_name,
                                         "postal_code_inquiry"),
                                data,
                                method="POST")
        return ResponseData.serialize(PostalCode, response)

    def persian_to_finglish(self, persian_text: str) -> ResponseData[Finglish]:
        """
        persian to finglish
        transform persian text to finglish text

        :param persian_text: Persian text
        :returns: if its successful returns finglish text.
        :rtype: ResponseData<Finglish>
        """
        data = PersianToFinglishRequest(persian_text=persian_text)
        response = self.request(make_url(self.service_name,
                                         "persian_to_finglish"),
                                data,
                                method="POST")
        return ResponseData.serialize(Finglish, response)

    def account_to_iban(self, bank_account: str,
                        bank_code: BankCode) -> ResponseData[IBan]:
        """
        account to iban
        Inquiry to retrive iban from bank_account

        :param bank_account: account number
        :param bank_code: BankCode
        :returns: returns Iban data.
        :rtype: ResponseData<IBan>
        """
        data = AccountToIBANRequest(bank_account=bank_account,
                                    bank_code=bank_code)
        response = self.request(make_url(self.service_name, "account_to_iban"),
                                data,
                                method="POST")
        return ResponseData.serialize(IBan, response)

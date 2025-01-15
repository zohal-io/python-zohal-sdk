from zohal_sdk import Client
from os import getenv

token = getenv("TOKEN")
client = Client(token)

matched = client.check_card_with_national_code(
    "0123456789",
    "1900/1/1",
    "1234123412341234"
)

print(matched.response_body.data.matched)

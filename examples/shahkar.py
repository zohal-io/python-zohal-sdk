from zohal_sdk import Client
from os import getenv

token = getenv("TOKEN")
client = Client(token)

matched = client.shahkar(
    "0123456789",
    "09000000000",
)

print(matched.response_body.data.matched)

from zohal_sdk import Client
from os import getenv

token = getenv("TOKEN")
client = Client(token)

person = client.national_identity_inquiry("0123456789",
                                          "1900/01/01",
                                          gender=True)

print(person.response_body.data.father_name)

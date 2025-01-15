from ..constants import BASE_URL


def make_url(service, function):
    return f"{BASE_URL}/v0/services/{service}/{function}"

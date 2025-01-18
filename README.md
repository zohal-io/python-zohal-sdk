# zohal-sdk
[![PyPi Package Version](https://img.shields.io/pypi/v/zohal-sdk.svg)](https://pypi.python.org/pypi/zohal-sdk)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/zohal-sdk.svg)](https://pypi.python.org/pypi/zohal-sdk)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![PyPi status](https://img.shields.io/pypi/status/zohal-sdk.svg?style=flat-square)](https://pypi.python.org/pypi/zohal-sdk)

## Overview

zohal-sdk is a Python SDK for interfacing with [zohal.io](https://zohal.io). It simplifies the process of interacting with the API by providing clean, Pythonic abstractions for all key functionalities.

## Installation

Install the SDK using pip:

```bash
pip install zohal-sdk
```
## Getting Started

Here's a quick example to get you started:
```python
from zohal_sdk import Client

# Initialize the client
client = Client(token="your_api_key")

# Example usage
response = client.shahkar(mobile="your mobile number", national_code="your national code")
print(response)
```
For detailed usage, check the documentation.
Documentation

## Documentation

Full documentation is available at [Documentation](https://zohal.io/documents).

## Contributing

We welcome contributions! See [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines.

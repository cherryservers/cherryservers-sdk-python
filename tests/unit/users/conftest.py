"""Cherry Servers Python SDK user unit test fixtures."""

from __future__ import annotations

import json

import pytest
import requests


@pytest.fixture(scope="package")
def get_user_successful_response() -> requests.Response:
    """Initialize successful response for user get."""
    response = requests.Response()
    response.status_code = 200
    response._content = json.dumps(
        {
            "id": 123456,
            "first_name": "",
            "last_name": "",
            "email": "example@example.com",
            "email_verified": False,
            "phone": "",
            "security_phone_verified": False,
            "state": "",
            "city": "",
            "country_iso_2": "LT",
            "href": "/users/123456",
            "security_phone": "",
            "skype_username": "",
            "linkedin_profile": "",
            "address_1": "",
            "address_2": "",
            "date_of_birth": "",
            "national_id_number": "",
        }
    ).encode("utf-8")
    return response

"""Cherry Servers Python SDK teams unit test fixtures."""

from __future__ import annotations

import json

import pytest
import requests


@pytest.fixture(scope="package")
def get_team_successful_response() -> requests.Response:
    """Initialize successful response for team get."""
    response = requests.Response()
    response.status_code = 200
    response._content = json.dumps(
        {
            "id": 123456,
            "name": " team",
            "credit": {
                "account": {"currency": "EUR"},
                "promo": {"remaining": 669.15, "usage": 6.65, "currency": "EUR"},
                "resources": {
                    "pricing": {
                        "price": 0.1228,
                        "taxed": True,
                        "currency": "EUR",
                        "unit": "Hourly",
                    },
                    "remaining": {"time": 6586, "unit": "Hourly"},
                },
            },
            "billing": {
                "type": "personal",
                "country_iso_2": "LT",
                "vat": {"amount": 21, "valid": False},
                "currency": "EUR",
            },
            "href": "/teams/123456",
        }
    ).encode("utf-8")
    return response


@pytest.fixture(scope="package")
def create_team_successful_response() -> requests.Response:
    """Initialize successful response for team create."""
    response = requests.Response()
    response.status_code = 201
    response._content = json.dumps(
        {
            "id": 159248,
            "name": "sdk-test",
            "credit": {
                "account": {"currency": "EUR"},
                "promo": {"currency": "EUR"},
                "resources": {
                    "pricing": {"taxed": True, "currency": "EUR", "unit": "Hourly"},
                    "remaining": {"unit": "Hourly"},
                },
            },
            "billing": {
                "type": "personal",
                "country_iso_2": "LT",
                "vat": {"amount": 21, "valid": False},
                "currency": "EUR",
            },
            "href": "/teams/159248",
        }
    ).encode("utf-8")
    return response


@pytest.fixture(scope="package")
def update_team_successful_response() -> requests.Response:
    """Initialize successful response for team update."""
    response = requests.Response()
    response.status_code = 201
    response._content = json.dumps(
        {
            "id": 159248,
            "name": "sdk-test-updated",
            "credit": {
                "account": {"currency": "EUR"},
                "promo": {"currency": "EUR"},
                "resources": {
                    "pricing": {"taxed": True, "currency": "EUR", "unit": "Hourly"},
                    "remaining": {"unit": "Hourly"},
                },
            },
            "billing": {
                "type": "personal",
                "country_iso_2": "LT",
                "vat": {"amount": 21, "valid": False},
                "currency": "EUR",
            },
            "href": "/teams/159248",
        }
    ).encode("utf-8")
    return response


@pytest.fixture(scope="package")
def get_all_teams_successful_response() -> requests.Response:
    """Initialize successful response for get all teams."""
    response = requests.Response()
    response.status_code = 200
    response._content = json.dumps(
        [
            {
                "id": 123456,
                "name": " team",
                "credit": {
                    "account": {"currency": "EUR"},
                    "promo": {"remaining": 669.06, "usage": 6.74, "currency": "EUR"},
                    "resources": {
                        "pricing": {
                            "price": 0.1228,
                            "taxed": True,
                            "currency": "EUR",
                            "unit": "Hourly",
                        },
                        "remaining": {"time": 6585, "unit": "Hourly"},
                    },
                },
                "billing": {
                    "type": "personal",
                    "country_iso_2": "LT",
                    "vat": {"amount": 21, "valid": False},
                    "currency": "EUR",
                },
                "href": "/teams/123456",
            },
            {
                "id": 654321,
                "name": "cherryservers-python-sdk-test",
                "credit": {
                    "account": {"currency": "EUR"},
                    "promo": {"currency": "EUR"},
                    "resources": {
                        "pricing": {"taxed": True, "currency": "EUR", "unit": "Hourly"},
                        "remaining": {"unit": "Hourly"},
                    },
                },
                "billing": {
                    "type": "personal",
                    "country_iso_2": "LT",
                    "vat": {"amount": 21, "valid": False},
                    "currency": "EUR",
                },
                "href": "/teams/654321",
            },
        ]
    ).encode("utf-8")
    return response

"""Cherry Servers Python SDK user unit test fixtures."""

from __future__ import annotations

from typing import Any
from unittest import mock

import pytest

import cherryservers_sdk_python.users


@pytest.fixture
def users_client() -> cherryservers_sdk_python.users.UserClient:
    """Initialize user client fixture."""
    return cherryservers_sdk_python.users.UserClient(api_client=mock.MagicMock())


@pytest.fixture
def user_resource(
    simple_user: dict[str, Any],
    users_client: cherryservers_sdk_python.users.UserClient,
) -> cherryservers_sdk_python.users.User:
    """Initialize user resource fixture."""
    return cherryservers_sdk_python.users.User(
        client=users_client,
        model=cherryservers_sdk_python.users.UserModel.model_validate(simple_user),
    )


@pytest.fixture
def simple_user() -> dict[str, Any]:
    """Initialize simple user fixture."""
    return {
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

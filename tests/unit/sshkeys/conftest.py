"""Cherry Servers Python SDK SSH keys unit test fixtures."""

from __future__ import annotations

from typing import Any
from unittest import mock

import pytest

import cherryservers_sdk_python.sshkeys


@pytest.fixture
def sshkeys_client() -> cherryservers_sdk_python.sshkeys.SSHKeyClient:
    """Initialize SSH key client fixture."""
    return cherryservers_sdk_python.sshkeys.SSHKeyClient(api_client=mock.MagicMock())


@pytest.fixture
def sshkey_resource(
    simple_sshkey: dict[str, Any],
    sshkeys_client: cherryservers_sdk_python.sshkeys.SSHKeyClient,
) -> cherryservers_sdk_python.sshkeys.SSHKey:
    """Initialize SSH key resource fixture."""
    return cherryservers_sdk_python.sshkeys.SSHKey(
        client=sshkeys_client,
        model=cherryservers_sdk_python.sshkeys.SSHKeyModel.model_validate(
            simple_sshkey
        ),
    )


@pytest.fixture
def simple_sshkey() -> dict[str, Any]:
    """Initialize simple SSH key fixture."""
    return {
        "id": 1234,
        "label": "my-key",
        "key": "ssh-ed25519 AAAAC3NzaC1lZDI1NTE...YE2VZhcmrFy1 example@example.com",
        "fingerprint": "e8:67:21:dd:f5:27:fb:2b:5c:cc:b4:07:34:6c:e6:2d",
        "user": {
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
            "ssh_keys": [
                {
                    "id": 1234,
                    "label": "my-key",
                    "key": "ssh-ed25519 AAAAC3NzaC1lZDI1NTE...YE2VZhcmrFy1 example@example.com",
                    "fingerprint": "e8:67:21:dd:f5:27:fb:2b:5c:cc:b4:07:34:6c:e6:2d",
                    "updated": "2024-07-16T12:12:05+00:00",
                    "created": "2024-07-16T12:12:05+00:00",
                    "href": "/ssh-keys/1234",
                }
            ],
        },
        "updated": "2024-07-16T12:12:05+00:00",
        "created": "2024-07-16T12:12:05+00:00",
        "href": "/ssh-keys/1234",
    }

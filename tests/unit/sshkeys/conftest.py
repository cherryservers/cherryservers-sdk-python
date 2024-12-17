"""Cherry Servers Python SDK SSH keys unit test fixtures."""

from __future__ import annotations

import json

import pytest
import requests


@pytest.fixture(scope="package")
def get_sshkey_response() -> requests.Response:
    """Initialize successful response for SSH key get request."""
    response = requests.Response()
    response.status_code = 200
    response._content = json.dumps(
        {
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
    ).encode("utf-8")
    return response


@pytest.fixture(scope="package")
def post_sshkey_response() -> requests.Response:
    """Initialize successful response for SSH key creation."""
    response = requests.Response()
    response.status_code = 201
    response._content = json.dumps(
        {
            "id": 1234,
            "label": "my-key",
            "key": "ssh-ed25519 AAAAC3NzaC1lZDI1NTE...YE2VZhcmrFy1 example@example.com",
            "fingerprint": "e8:67:21:dd:f5:27:fb:2b:5c:cc:b4:07:34:6c:e6:2d",
            "updated": "2024-07-16T12:12:05+00:00",
            "created": "2024-07-16T12:12:05+00:00",
            "href": "/ssh-keys/1234",
        }
    ).encode("utf-8")
    return response


@pytest.fixture(scope="package")
def put_sshkey_response() -> requests.Response:
    """Initialize successful response for SSH update request."""
    response = requests.Response()
    response.status_code = 201
    response._content = json.dumps(
        {
            "id": 1234,
            "label": "my-key-updated",
            "key": "ssh-ed25519 AAAAC3NzaC1lZDI1NTE...YEasg4ZhcmrFy1 example@example.com",
            "fingerprint": "e8:67:21:dd:f5:27:fb:2b:8b:cc:b4:07:34:6c:e6:2d",
            "updated": "2024-07-16T12:12:06+00:00",
            "created": "2024-07-16T12:12:05+00:00",
            "href": "/ssh-keys/1234",
        }
    ).encode("utf-8")
    return response


@pytest.fixture(scope="package")
def get_sshkey_after_update_response() -> requests.Response:
    """Initialize successful response for SSH key get request."""
    response = requests.Response()
    response.status_code = 200
    response._content = json.dumps(
        {
            "id": 1234,
            "label": "my-key-updated",
            "key": "ssh-ed25519 AAAAC3NzaC1lZDI1NTE...YEasg4ZhcmrFy1 example@example.com",
            "fingerprint": "e8:67:21:dd:f5:27:fb:2b:8b:cc:b4:07:34:6c:e6:2d",
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
                        "label": "my-key-updated",
                        "key": "ssh-ed25519 AAAAC3NzaC1lZDI1NTE...YEasg4ZhcmrFy1 example@example.com",
                        "fingerprint": "e8:67:21:dd:f5:27:fb:2b:8b:cc:b4:07:34:6c:e6:2d",
                        "updated": "2024-07-16T12:12:06+00:00",
                        "created": "2024-07-16T12:12:05+00:00",
                        "href": "/ssh-keys/1234",
                    }
                ],
            },
            "updated": "2024-07-16T12:12:06+00:00",
            "created": "2024-07-16T12:12:05+00:00",
            "href": "/ssh-keys/1234",
        }
    ).encode("utf-8")
    return response


@pytest.fixture(scope="package")
def list_sshkeys_response() -> requests.Response:
    """Initialize successful response for getting all SSH keys."""
    response = requests.Response()
    response.status_code = 200
    response._content = json.dumps(
        [
            {
                "id": 4321,
                "label": "my-key",
                "key": "ssh-ed25519 AAAAC3NzaC1lZDI1NTEfk5...YE2VZhcmrFy1 example@example.com",
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
                            "key": "ssh-ed25519 AAAAC3NzaC1lZDI1NTEfk5...YE2VZhcmrFy1 example@example.com",
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
            },
            {
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
            },
        ]
    ).encode("utf-8")
    return response

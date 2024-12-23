"""Unit tests for Cherry Servers Python SDK user client."""

from __future__ import annotations

from typing import cast
from unittest import mock

import cherryservers_sdk_python.users
from tests.unit import helpers


def test_get_current_user_success(
    simple_user: helpers.JSON, users_client: cherryservers_sdk_python.users.UserClient
) -> None:
    """Test successfully getting current user."""
    expected_api_resp = helpers.build_api_response(simple_user, 200)
    cast(mock.Mock, users_client._api_client.get).return_value = expected_api_resp
    user = users_client.get_current_user()

    assert user.get_model() == cherryservers_sdk_python.users.UserModel.model_validate(
        simple_user
    )

    cast(mock.Mock, users_client._api_client.get).assert_called_with(
        "user",
        None,
        users_client.request_timeout,
    )


def test_get_by_id_success(
    simple_user: helpers.JSON, users_client: cherryservers_sdk_python.users.UserClient
) -> None:
    """Test successfully getting a user by ID."""
    expected_api_resp = helpers.build_api_response(simple_user, 200)
    cast(mock.Mock, users_client._api_client.get).return_value = expected_api_resp
    user = users_client.get_by_id(helpers.get_integer_id(simple_user))

    assert user.get_model() == cherryservers_sdk_python.users.UserModel.model_validate(
        simple_user
    )

    cast(mock.Mock, users_client._api_client.get).assert_called_with(
        f"users/{helpers.get_integer_id(simple_user)}",
        None,
        users_client.request_timeout,
    )

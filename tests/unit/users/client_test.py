"""Unit tests for Cherry Servers Python SDK user client."""

from __future__ import annotations

from typing import TYPE_CHECKING
from unittest import mock

import pytest

import cherryservers_sdk_python.users
from tests.unit import resource_client_helpers

if TYPE_CHECKING:
    import requests


class TestClient:
    """Test user client."""

    @pytest.fixture
    def users_client(self) -> cherryservers_sdk_python.users.UserClient:
        """Initialize user client fixture."""
        return cherryservers_sdk_python.users.UserClient(api_client=mock.MagicMock())

    def test_get_current_user_success(
        self,
        get_user_successful_response: requests.Response,
        users_client: cherryservers_sdk_python.users.UserClient,
    ) -> None:
        """Test successfully getting current user."""
        resource_client_helpers.check_getter_function(
            get_user_successful_response,
            users_client,
            users_client.get_current_user,
        )

    def test_get_by_id_success(
        self,
        get_user_successful_response: requests.Response,
        users_client: cherryservers_sdk_python.users.UserClient,
    ) -> None:
        """Test successfully getting a user by ID."""
        resource_client_helpers.check_getter_function(
            get_user_successful_response,
            users_client,
            lambda: users_client.get_by_id(123456),
        )


class TestUser:
    """Test user resource."""

    @pytest.fixture
    def user(
        self, get_user_successful_response: requests.Response
    ) -> cherryservers_sdk_python.users.User:
        """Initialize user fixture."""
        return cherryservers_sdk_python.users.User(
            client=mock.MagicMock(),
            model=cherryservers_sdk_python.users.UserModel.model_validate(
                get_user_successful_response.json()
            ),
        )

    def test_get_id(
        self,
        user: cherryservers_sdk_python.users.User,
        get_user_successful_response: requests.Response,
    ) -> None:
        """Test getting user ID."""
        assert user.get_id() == get_user_successful_response.json()["id"]

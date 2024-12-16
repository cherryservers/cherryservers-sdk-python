"""Unit tests for Cherry Servers Python SDK user client."""

from __future__ import annotations

from typing import TYPE_CHECKING, cast
from unittest import mock

import pytest

import cherryservers_sdk_python.users

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
        """Test successful current user get."""
        cast(
            mock.Mock, users_client._api_client.get
        ).return_value = get_user_successful_response
        user = users_client.get_current_user()
        user_expected_model = cherryservers_sdk_python.users.UserModel.model_validate(
            get_user_successful_response.json()
        )
        assert user_expected_model == user.get_model()

    def test_get_by_id_success(
        self,
        get_user_successful_response: requests.Response,
        users_client: cherryservers_sdk_python.users.UserClient,
    ) -> None:
        """Test successful user get by ID."""
        cast(
            mock.Mock, users_client._api_client.get
        ).return_value = get_user_successful_response
        user = users_client.get_by_id(123456)
        user_expected_model = cherryservers_sdk_python.users.UserModel.model_validate(
            get_user_successful_response.json()
        )
        assert user_expected_model == user.get_model()


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

    def test_get_model(self, user: cherryservers_sdk_python.users.User) -> None:
        """Test getting user model."""
        assert user.get_model() == user._model

    def test_get_id(
        self,
        user: cherryservers_sdk_python.users.User,
        get_user_successful_response: requests.Response,
    ) -> None:
        """Test getting user ID."""
        assert user.get_id() == get_user_successful_response.json()["id"]

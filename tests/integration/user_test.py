"""Test cherryservers_sdk_python users module functionality."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import cherryservers_sdk_python


class TestUser:
    """Test User functionality."""

    def test_get_current_user(
        self, facade: cherryservers_sdk_python.facade.CherryApiFacade
    ) -> None:
        """Test getting current user."""
        user = facade.users.get_current_user()

        assert user.get_model().id

    def test_get_by_id(
        self, facade: cherryservers_sdk_python.facade.CherryApiFacade
    ) -> None:
        """Test getting user by id."""
        user = facade.users.get_current_user()

        facade.users.get_by_id(user.get_model().id)

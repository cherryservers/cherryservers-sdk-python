"""Unit tests for Cherry Servers Python SDK user resource."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import cherryservers_sdk_python.users


def test_get_id(
    user_resource: cherryservers_sdk_python.users.User,
) -> None:
    """Test getting user resource ID."""
    assert user_resource.get_id() == user_resource.get_model().id

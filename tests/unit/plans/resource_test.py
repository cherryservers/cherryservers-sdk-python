"""Unit tests for Cherry Servers Python SDK plan resource."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import cherryservers_sdk_python.plans


def test_get_id(
    plan_resource: cherryservers_sdk_python.plans.Plan,
) -> None:
    """Test getting plan resource ID."""
    assert plan_resource.get_id() == plan_resource.get_model().id

"""Unit tests for Cherry Servers Python SDK region resource."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import cherryservers_sdk_python.regions


def test_get_id(
    region_resource: cherryservers_sdk_python.regions.Region,
) -> None:
    """Test getting region resource ID."""
    assert region_resource.get_id() == region_resource.get_model().id

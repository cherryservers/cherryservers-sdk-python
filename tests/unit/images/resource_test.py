"""Unit tests for Cherry Servers Python SDK image resource."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import cherryservers_sdk_python.images


def test_get_id(
    image_resource: cherryservers_sdk_python.images.Image,
) -> None:
    """Test getting image resource ID."""
    assert image_resource.get_id() == image_resource.get_model().id

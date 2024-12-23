"""Cherry Servers Python SDK regions unit test fixtures."""

from __future__ import annotations

from typing import Any
from unittest import mock

import pytest

import cherryservers_sdk_python.images


@pytest.fixture
def images_client() -> cherryservers_sdk_python.images.ImageClient:
    """Initialize image client fixture."""
    return cherryservers_sdk_python.images.ImageClient(api_client=mock.MagicMock())


@pytest.fixture
def image_resource(
    simple_image: dict[str, Any],
    images_client: cherryservers_sdk_python.images.ImageClient,
) -> cherryservers_sdk_python.images.Image:
    """Initialize image resource fixture."""
    return cherryservers_sdk_python.images.Image(
        client=images_client,
        model=cherryservers_sdk_python.images.ImageModel.model_validate(simple_image),
    )


@pytest.fixture
def simple_image() -> dict[str, Any]:
    """Initialize simple image fixture."""
    return {"id": 40785, "name": "Debian 12 64bit", "slug": "debian_12_64bit"}

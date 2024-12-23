"""Cherry Servers Python SDK regions unit test fixtures."""

from __future__ import annotations

from typing import Any
from unittest import mock

import pytest

import cherryservers_sdk_python.regions


@pytest.fixture
def regions_client() -> cherryservers_sdk_python.regions.RegionClient:
    """Initialize region client fixture."""
    return cherryservers_sdk_python.regions.RegionClient(api_client=mock.MagicMock())


@pytest.fixture
def region_resource(
    simple_region: dict[str, Any],
    regions_client: cherryservers_sdk_python.regions.RegionClient,
) -> cherryservers_sdk_python.regions.Region:
    """Initialize region resource fixture."""
    return cherryservers_sdk_python.regions.Region(
        client=regions_client,
        model=cherryservers_sdk_python.regions.RegionModel.model_validate(
            simple_region
        ),
    )


@pytest.fixture
def simple_region() -> dict[str, Any]:
    """Initialize simple region fixture."""
    return {
        "id": 1,
        "name": "EU-Nord-1",
        "slug": "eu_nord_1",
        "region_iso_2": "LT",
        "href": "/regions/1",
        "bgp": {"hosts": ["123.123.123.123", "123.123.123.123"], "asn": 12345},
        "location": "Lithuania, Šiauliai",
    }

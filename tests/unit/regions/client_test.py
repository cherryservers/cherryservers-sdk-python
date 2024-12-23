"""Unit tests for Cherry Servers Python SDK region client."""

from __future__ import annotations

from typing import cast
from unittest import mock

import cherryservers_sdk_python.regions
from tests.unit import helpers


def test_get_by_id_success(
    simple_region: helpers.JSON,
    regions_client: cherryservers_sdk_python.regions.RegionClient,
) -> None:
    """Test successfully getting a region by ID."""
    expected_api_resp = helpers.build_api_response(simple_region, 200)
    cast(mock.Mock, regions_client._api_client.get).return_value = expected_api_resp
    region = regions_client.get_by_id(helpers.get_integer_id(simple_region))

    assert (
        region.get_model()
        == cherryservers_sdk_python.regions.RegionModel.model_validate(simple_region)
    )

    cast(mock.Mock, regions_client._api_client.get).assert_called_with(
        f"regions/{helpers.get_integer_id(simple_region)}",
        None,
        regions_client.request_timeout,
    )


def test_get_all_success(
    simple_region: helpers.JSON,
    regions_client: cherryservers_sdk_python.regions.RegionClient,
) -> None:
    """Test successfully getting all regions."""
    expected_api_resp = helpers.build_api_response([simple_region, simple_region], 200)
    cast(mock.Mock, regions_client._api_client.get).return_value = expected_api_resp
    regions = regions_client.get_all()

    for region, expected_region in zip(regions, [simple_region, simple_region]):
        assert (
            region.get_model()
            == cherryservers_sdk_python.regions.RegionModel.model_validate(
                expected_region
            )
        )

    cast(mock.Mock, regions_client._api_client.get).assert_called_with(
        "regions", None, regions_client.request_timeout
    )

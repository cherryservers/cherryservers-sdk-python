"""Unit tests for Cherry Servers Python SDK image client."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, cast

import cherryservers_sdk_python.images
from tests.unit import helpers

if TYPE_CHECKING:
    from unittest import mock


def test_list_by_plan_success(
    simple_image: dict[str, Any],
    images_client: cherryservers_sdk_python.images.ImageClient,
) -> None:
    """Test successfully listing images by plan."""
    expected_api_resp = helpers.build_api_response([simple_image, simple_image], 200)
    cast("mock.Mock", images_client._api_client.get).return_value = expected_api_resp
    images = images_client.list_by_plan("cloud_vps_1")

    for image, expected_image in zip(
        images, [simple_image, simple_image], strict=False
    ):
        assert (
            image.get_model()
            == cherryservers_sdk_python.images.ImageModel.model_validate(expected_image)
        )

    cast("mock.Mock", images_client._api_client.get).assert_called_with(
        "plans/cloud_vps_1/images", None, images_client.request_timeout
    )

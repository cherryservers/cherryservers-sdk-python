"""Helper functions for resource tests."""

from __future__ import annotations

from typing import TYPE_CHECKING, Callable, cast
from unittest import mock

from cherryservers_sdk_python import _base

if TYPE_CHECKING:
    import requests


def check_update_function[C: _base.ResourceClient, M: _base.ResourceModel](
    expected_put_resp: requests.Response,
    expected_get_resp: requests.Response,
    resource: _base.Resource[C, M],
    resource_update_hook: Callable[[], None],
) -> None:
    """Test successfully updating a resource.

    :param requests.Response expected_put_resp:
     Expected response from the API for the PUT update request.
     This response must contain JSON that can be deserialized into a
     valid resource model.
    :param requests.Response expected_get_resp:
     Expected response from the API for the GET that occurs after update.
     This response must contain JSON that can be deserialized into a
     valid resource model.
    :param _base.Resource[C, M] resource: Resource under test.
    :param Callable[[], _base.Resource[C, M]] resource_update_hook:
     Hook for resource function that updates it. This function must use
     the same resource instance as the one passed to this function.
    """
    cast(mock.Mock, resource._client._api_client.get).return_value = expected_get_resp
    cast(mock.Mock, resource._client._api_client.put).return_value = expected_put_resp

    resource_update_hook()

    assert resource.get_model() == resource.get_model().model_validate(
        expected_get_resp.json()
    )

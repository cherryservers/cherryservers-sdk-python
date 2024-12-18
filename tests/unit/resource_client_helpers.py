"""Helper functions for resource client tests."""

from __future__ import annotations

from typing import TYPE_CHECKING, Callable, Sequence, cast
from unittest import mock

from cherryservers_sdk_python import _base

if TYPE_CHECKING:
    import requests


def check_listing_function[C: _base.ResourceClient, M: _base.ResourceModel](
    expected_response: requests.Response,
    resource_client: C,
    resource_listing_hook: Callable[[], Sequence[_base.Resource[C, M]]],
) -> None:
    """Test successfully getting all expected resources.

    :param requests.Response expected_response: Expected response from the API.
     This response must contain JSON that can be deserialized into an Iterable
     of valid resource models.
    :param C resource_client: Resource client.
    :param Callable[[], Sequence[_base.Resource[C, M]]] resource_listing_hook:
     Hook for client function that lists resources. This function must use
     the same resource client instance as the one passed to this function.
    """
    cast(mock.Mock, resource_client._api_client.get).return_value = expected_response
    resources = resource_listing_hook()
    for resource, resp in zip(resources, expected_response.json()):
        assert resource.get_model() == resource.get_model().model_validate(resp)


def check_getter_function[
    C: _base.ResourceClient,
    M: _base.ResourceModel,
](
    expected_response: requests.Response,
    resource_client: C,
    resource_retrieval_hook: Callable[[], _base.Resource[C, M]],
) -> None:
    """Test successfully getting a single resource.

    :param requests.Response expected_response: Expected response from the API.
     This response must contain JSON that can be deserialized into a
     valid resource model.
    :param C resource_client: Resource client.
    :param Callable[[], _base.Resource[C, M]] resource_retrieval_hook:
     Hook for client function that retrieves a resource. This function must use
     the same resource client instance as the one passed to this function.
    """
    cast(mock.Mock, resource_client._api_client.get).return_value = expected_response
    resource = resource_retrieval_hook()
    assert resource.get_model() == resource.get_model().model_validate(
        expected_response.json()
    )


def check_creation_function[C: _base.ResourceClient, M: _base.ResourceModel](
    expected_post_resp: requests.Response,
    expected_get_resp: requests.Response,
    resource_client: C,
    resource_creation_hook: Callable[[], _base.Resource[C, M]],
) -> None:
    """Test successfully creating a resource.

    :param requests.Response expected_post_resp:
     Expected response from the API for the POST creation request.
     This response must contain JSON that can be deserialized into a
     valid resource model.
    :param requests.Response expected_get_resp:
     Expected response from the API for the GET that occurs after creation.
     This response must contain JSON that can be deserialized into a
     valid resource model.
    :param C resource_client: Resource client.
    :param Callable[[], _base.Resource[C, M]] resource_creation_hook:
     Hook for client function that creates a resource. This function must use
     the same resource client instance as the one passed to this function.
    """
    cast(mock.Mock, resource_client._api_client.get).return_value = expected_get_resp
    cast(mock.Mock, resource_client._api_client.post).return_value = expected_post_resp

    resource = resource_creation_hook()

    assert resource.get_model() == resource.get_model().model_validate(
        expected_get_resp.json()
    )


def check_update_function[C: _base.ResourceClient, M: _base.ResourceModel](
    expected_put_resp: requests.Response,
    expected_get_resp: requests.Response,
    resource_client: C,
    resource_update_hook: Callable[[], _base.Resource[C, M]],
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
    :param C resource_client: Resource client.
    :param Callable[[], _base.Resource[C, M]] resource_update_hook:
     Hook for client function that updates a resource. This function must use
     the same resource client instance as the one passed to this function.
    """
    cast(mock.Mock, resource_client._api_client.get).return_value = expected_get_resp
    cast(mock.Mock, resource_client._api_client.put).return_value = expected_put_resp

    resource = resource_update_hook()

    assert resource.get_model() == resource.get_model().model_validate(
        expected_get_resp.json()
    )

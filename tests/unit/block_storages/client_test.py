"""Unit tests for Cherry Servers Python SDK block storages client."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, cast

import cherryservers_sdk_python
from tests.unit import helpers

if TYPE_CHECKING:
    from unittest import mock


def test_get_by_id_success(
    simple_block_storage: dict[str, Any],
    block_storages_client: cherryservers_sdk_python.block_storages.BlockStorageClient,
) -> None:
    """Test successfully getting a block storage by ID."""
    expected_api_resp = helpers.build_api_response(simple_block_storage, 200)
    cast(
        "mock.Mock", block_storages_client._api_client.get
    ).return_value = expected_api_resp
    project = block_storages_client.get_by_id(simple_block_storage["id"])

    assert (
        project.get_model()
        == cherryservers_sdk_python.block_storages.BlockStorageModel.model_validate(
            simple_block_storage
        )
    )

    cast("mock.Mock", block_storages_client._api_client.get).assert_called_with(
        f"storages/{simple_block_storage['id']}",
        None,
        block_storages_client.request_timeout,
    )


def test_list_by_project_success(
    simple_block_storage: dict[str, Any],
    block_storages_client: cherryservers_sdk_python.block_storages.BlockStorageClient,
) -> None:
    """Test successfully listing block storages by project ID."""
    expected_api_resp = helpers.build_api_response(
        [simple_block_storage, simple_block_storage], 200
    )
    cast(
        "mock.Mock", block_storages_client._api_client.get
    ).return_value = expected_api_resp
    block_storages = block_storages_client.list_by_project(123456)

    for block_storage, expected_block_storage in zip(
        block_storages, [simple_block_storage, simple_block_storage], strict=False
    ):
        assert (
            block_storage.get_model()
            == cherryservers_sdk_python.block_storages.BlockStorageModel.model_validate(
                expected_block_storage
            )
        )

    cast("mock.Mock", block_storages_client._api_client.get).assert_called_with(
        "projects/123456/storages",
        None,
        block_storages_client.request_timeout,
    )


def test_create_success(
    block_storages_client: cherryservers_sdk_python.block_storages.BlockStorageClient,
    simple_block_storage: dict[str, Any],
) -> None:
    """Test successfully creating a block storage."""
    creation_request = cherryservers_sdk_python.block_storages.CreationRequest(
        region="eu_nord_1", size=1
    )

    get_response = helpers.build_api_response(simple_block_storage, 200)
    post_response = helpers.build_api_response(simple_block_storage, 201)
    cast(
        "mock.Mock", block_storages_client._api_client.post
    ).return_value = post_response
    cast("mock.Mock", block_storages_client._api_client.get).return_value = get_response

    block_storage = block_storages_client.create(creation_request, 123456)

    assert (
        block_storage.get_model()
        == cherryservers_sdk_python.block_storages.BlockStorageModel.model_validate(
            simple_block_storage
        )
    )

    cast("mock.Mock", block_storages_client._api_client.post).assert_called_with(
        "projects/123456/storages",
        creation_request,
        None,
        block_storages_client.request_timeout,
    )

    cast("mock.Mock", block_storages_client._api_client.get).assert_called_with(
        f"storages/{simple_block_storage['id']}",
        None,
        block_storages_client.request_timeout,
    )


def test_update_success(
    simple_block_storage: dict[str, Any],
    block_storages_client: cherryservers_sdk_python.block_storages.BlockStorageClient,
) -> None:
    """Test successfully updating a block storage."""
    update_req = cherryservers_sdk_python.block_storages.UpdateRequest(
        size=1, description=""
    )

    cast(
        "mock.Mock", block_storages_client._api_client.get
    ).return_value = helpers.build_api_response(simple_block_storage, 200)
    cast(
        "mock.Mock", block_storages_client._api_client.put
    ).return_value = helpers.build_api_response(simple_block_storage, 201)

    block_storage = block_storages_client.update(simple_block_storage["id"], update_req)

    assert (
        block_storage.get_model()
        == cherryservers_sdk_python.block_storages.BlockStorageModel.model_validate(
            simple_block_storage
        )
    )

    cast("mock.Mock", block_storages_client._api_client.get).assert_called_with(
        f"storages/{simple_block_storage['id']}",
        None,
        block_storages_client.request_timeout,
    )

    cast("mock.Mock", block_storages_client._api_client.put).assert_called_once_with(
        f"storages/{simple_block_storage['id']}",
        update_req,
        None,
        block_storages_client._request_timeout,
    )


def test_attach_success(
    attached_block_storage: dict[str, Any],
    block_storages_client: cherryservers_sdk_python.block_storages.BlockStorageClient,
) -> None:
    """Test successfully attach block storage to a server."""
    attach_req = cherryservers_sdk_python.block_storages.AttachRequest(attach_to=622711)

    get_response = helpers.build_api_response(attached_block_storage, 200)
    post_response = helpers.build_api_response(attached_block_storage, 201)
    cast(
        "mock.Mock", block_storages_client._api_client.post
    ).return_value = post_response
    cast("mock.Mock", block_storages_client._api_client.get).return_value = get_response

    block_storage = block_storages_client.attach(
        attached_block_storage["id"], attach_req
    )

    assert (
        block_storage.get_model()
        == cherryservers_sdk_python.block_storages.BlockStorageModel.model_validate(
            attached_block_storage
        )
    )

    cast("mock.Mock", block_storages_client._api_client.post).assert_called_with(
        f"storages/{attached_block_storage['id']}/attachments",
        attach_req,
        None,
        block_storages_client.request_timeout,
    )

    cast("mock.Mock", block_storages_client._api_client.get).assert_called_with(
        f"storages/{attached_block_storage['id']}",
        None,
        block_storages_client.request_timeout,
    )


def test_detach_success(
    simple_block_storage: dict[str, Any],
    block_storages_client: cherryservers_sdk_python.block_storages.BlockStorageClient,
) -> None:
    """Test successfully detaching a block storage from a server."""
    get_response = helpers.build_api_response(simple_block_storage, 200)
    cast("mock.Mock", block_storages_client._api_client.get).return_value = get_response

    block_storage = block_storages_client.detach(simple_block_storage["id"])

    assert (
        block_storage.get_model()
        == cherryservers_sdk_python.block_storages.BlockStorageModel.model_validate(
            simple_block_storage
        )
    )

    cast("mock.Mock", block_storages_client._api_client.delete).assert_called_with(
        f"storages/{simple_block_storage['id']}/attachments",
        None,
        block_storages_client.request_timeout,
    )

    cast("mock.Mock", block_storages_client._api_client.get).assert_called_with(
        f"storages/{simple_block_storage['id']}",
        None,
        block_storages_client.request_timeout,
    )


def test_delete_success(
    simple_block_storage: dict[str, Any],
    block_storages_client: cherryservers_sdk_python.block_storages.BlockStorageClient,
) -> None:
    """Test successfully deleting a block storage."""
    cast(
        "mock.Mock", block_storages_client._api_client.delete
    ).return_value = helpers.build_api_response({}, 204)

    block_storages_client.delete(simple_block_storage["id"])

    cast("mock.Mock", block_storages_client._api_client.delete).assert_called_once_with(
        f"storages/{simple_block_storage['id']}",
        None,
        block_storages_client._request_timeout,
    )

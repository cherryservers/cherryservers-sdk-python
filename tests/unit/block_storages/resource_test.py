"""Unit tests for Cherry Servers Python SDK block storage resource."""

from __future__ import annotations

import copy
from typing import Any, cast
from unittest import mock

import cherryservers_sdk_python.block_storages
from tests.unit import helpers


def test_get_id(
    block_storage_resource: cherryservers_sdk_python.block_storages.BlockStorage,
) -> None:
    """Test getting block storage resource ID."""
    assert block_storage_resource.get_id() == block_storage_resource.get_model().id


def test_update(
    block_storage_resource: cherryservers_sdk_python.block_storages.BlockStorage,
    simple_block_storage: dict[str, Any],
) -> None:
    """Test updating a block storage resource."""
    update_req = cherryservers_sdk_python.block_storages.UpdateRequest(
        size=2, description="updated-description"
    )

    updated_block_storage = copy.deepcopy(simple_block_storage)
    updated_block_storage["size"] = 2
    updated_block_storage["description"] = "updated-description"

    cast(
        mock.Mock, block_storage_resource._client._api_client.get
    ).return_value = helpers.build_api_response(updated_block_storage, 200)
    cast(
        mock.Mock, block_storage_resource._client._api_client.put
    ).return_value = helpers.build_api_response(updated_block_storage, 201)

    block_storage_resource.update(update_req)

    assert (
        block_storage_resource.get_model()
        == cherryservers_sdk_python.block_storages.BlockStorageModel.model_validate(
            updated_block_storage
        )
    )

    cast(mock.Mock, block_storage_resource._client._api_client.get).assert_called_with(
        f"storages/{simple_block_storage['id']}",
        None,
        block_storage_resource._client.request_timeout,
    )

    cast(
        mock.Mock, block_storage_resource._client._api_client.put
    ).assert_called_once_with(
        f"storages/{simple_block_storage['id']}",
        update_req,
        None,
        block_storage_resource._client._request_timeout,
    )


def test_attach(
    block_storage_resource: cherryservers_sdk_python.block_storages.BlockStorage,
    attached_block_storage: dict[str, Any],
) -> None:
    """Test attaching a block storage resource to a server."""
    attach_req = cherryservers_sdk_python.block_storages.AttachRequest(attach_to=622711)

    get_response = helpers.build_api_response(attached_block_storage, 200)
    post_response = helpers.build_api_response(attached_block_storage, 201)
    cast(
        mock.Mock, block_storage_resource._client._api_client.post
    ).return_value = post_response
    cast(
        mock.Mock, block_storage_resource._client._api_client.get
    ).return_value = get_response

    block_storage_resource.attach(attach_req)

    assert (
        block_storage_resource.get_model()
        == cherryservers_sdk_python.block_storages.BlockStorageModel.model_validate(
            attached_block_storage
        )
    )

    cast(mock.Mock, block_storage_resource._client._api_client.get).assert_called_with(
        f"storages/{attached_block_storage['id']}",
        None,
        block_storage_resource._client.request_timeout,
    )

    cast(
        mock.Mock, block_storage_resource._client._api_client.post
    ).assert_called_once_with(
        f"storages/{attached_block_storage['id']}/attachments",
        attach_req,
        None,
        block_storage_resource._client._request_timeout,
    )


def test_delete(
    block_storage_resource: cherryservers_sdk_python.block_storages.BlockStorage,
    simple_block_storage: dict[str, Any],
) -> None:
    """Test deleting a block storage resource."""
    cast(
        mock.Mock, block_storage_resource._client._api_client.delete
    ).return_value = helpers.build_api_response({}, 204)

    block_storage_resource.delete()

    cast(
        mock.Mock, block_storage_resource._client._api_client.delete
    ).assert_called_once_with(
        f"storages/{simple_block_storage['id']}",
        None,
        block_storage_resource._client._request_timeout,
    )

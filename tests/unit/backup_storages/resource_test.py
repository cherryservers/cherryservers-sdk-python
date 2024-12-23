"""Unit tests for Cherry Servers Python SDK backup storage resource."""

from __future__ import annotations

import copy
from typing import Any, cast
from unittest import mock

import cherryservers_sdk_python
from tests.unit import helpers


def test_get_id(
    backup_storage_resource: cherryservers_sdk_python.backup_storages.BackupStorage,
) -> None:
    """Test getting backup storage resource ID."""
    assert backup_storage_resource.get_id() == backup_storage_resource.get_model().id


def test_update(
    backup_storage_resource: cherryservers_sdk_python.backup_storages.BackupStorage,
    simple_backup_storage: dict[str, Any],
) -> None:
    """Test updating a backup storage resource."""
    update_req = cherryservers_sdk_python.backup_storages.UpdateRequest(
        slug="backup_100"
    )

    updated_backup_storage = copy.deepcopy(simple_backup_storage)
    updated_backup_storage["slug"] = "backup_100"
    updated_backup_storage["size_gigabytes"] = 100

    simple_backup_storage["status"] = "provisioning"

    cast(
        mock.Mock, backup_storage_resource._client._api_client.get
    ).return_value = helpers.build_api_response(updated_backup_storage, 200)
    cast(
        mock.Mock, backup_storage_resource._client._api_client.put
    ).return_value = helpers.build_api_response(simple_backup_storage, 201)

    backup_storage_resource.update(update_req)

    assert (
        backup_storage_resource.get_model()
        == cherryservers_sdk_python.backup_storages.BackupStorageModel.model_validate(
            updated_backup_storage
        )
    )

    cast(mock.Mock, backup_storage_resource._client._api_client.get).assert_called_with(
        f"backup-storages/{simple_backup_storage['id']}",
        {
            "fields": "available_addresses,ip,region,project,"
            "href,targeted_to,hostname,id,bgp,status,state,"
            "private_ip,public_ip,size_gigabytes,used_gigabytes,"
            "methods,rules,plan,pricing,name,"
            "whitelist,enabled,processing"
        },
        backup_storage_resource._client.request_timeout,
    )

    cast(
        mock.Mock, backup_storage_resource._client._api_client.put
    ).assert_called_once_with(
        f"backup-storages/{simple_backup_storage['id']}",
        update_req,
        None,
        backup_storage_resource._client._request_timeout,
    )


def test_update_access_method(
    backup_storage_resource: cherryservers_sdk_python.backup_storages.BackupStorage,
    simple_backup_storage: dict[str, Any],
) -> None:
    """Test updating a backup storage resources access method."""
    update_req = cherryservers_sdk_python.backup_storages.UpdateAccessMethodsRequest(
        enabled=True
    )

    cast(
        mock.Mock, backup_storage_resource._client._api_client.get
    ).return_value = helpers.build_api_response(simple_backup_storage, 200)
    cast(
        mock.Mock, backup_storage_resource._client._api_client.patch
    ).return_value = helpers.build_api_response(simple_backup_storage, 200)

    backup_storage_resource.update_access_method(update_req, "ftp")

    assert (
        backup_storage_resource.get_model()
        == cherryservers_sdk_python.backup_storages.BackupStorageModel.model_validate(
            simple_backup_storage
        )
    )

    cast(mock.Mock, backup_storage_resource._client._api_client.get).assert_called_with(
        f"backup-storages/{simple_backup_storage['id']}",
        {
            "fields": "available_addresses,ip,region,project,"
            "href,targeted_to,hostname,id,bgp,status,state,"
            "private_ip,public_ip,size_gigabytes,used_gigabytes,"
            "methods,rules,plan,pricing,name,"
            "whitelist,enabled,processing"
        },
        backup_storage_resource._client.request_timeout,
    )

    cast(
        mock.Mock, backup_storage_resource._client._api_client.patch
    ).assert_called_once_with(
        f"backup-storages/{simple_backup_storage['id']}/methods/ftp",
        update_req,
        None,
        backup_storage_resource._client._request_timeout,
    )


def test_delete(
    backup_storage_resource: cherryservers_sdk_python.backup_storages.BackupStorage,
    simple_backup_storage: dict[str, Any],
) -> None:
    """Test deleting a backup storage resource."""
    cast(
        mock.Mock, backup_storage_resource._client._api_client.delete
    ).return_value = helpers.build_api_response({}, 204)

    backup_storage_resource.delete()

    cast(
        mock.Mock, backup_storage_resource._client._api_client.delete
    ).assert_called_once_with(
        f"backup-storages/{simple_backup_storage['id']}",
        None,
        backup_storage_resource._client._request_timeout,
    )

"""Unit tests for Cherry Servers Python SDK backup storages client."""

from __future__ import annotations

import copy
from typing import Any, cast
from unittest import mock

import cherryservers_sdk_python
from tests.unit import helpers


def test_get_by_id_success(
    simple_backup_storage: dict[str, Any],
    backup_storages_client: cherryservers_sdk_python.backup_storages.BackupStorageClient,
) -> None:
    """Test successfully getting a block backup storage by ID."""
    expected_api_resp = helpers.build_api_response(simple_backup_storage, 200)
    cast(
        mock.Mock, backup_storages_client._api_client.get
    ).return_value = expected_api_resp
    backup_storage = backup_storages_client.get_by_id(simple_backup_storage["id"])

    assert (
        backup_storage.get_model()
        == cherryservers_sdk_python.backup_storages.BackupStorageModel.model_validate(
            simple_backup_storage
        )
    )

    cast(mock.Mock, backup_storages_client._api_client.get).assert_called_with(
        f"backup-storages/{simple_backup_storage['id']}",
        {
            "fields": "available_addresses,ip,region,project,"
            "href,targeted_to,hostname,id,bgp,status,state,"
            "private_ip,public_ip,size_gigabytes,used_gigabytes,"
            "methods,rules,plan,pricing,name,"
            "whitelist,enabled,processing"
        },
        backup_storages_client.request_timeout,
    )


def test_list_by_project_success(
    simple_backup_storage: dict[str, Any],
    backup_storages_client: cherryservers_sdk_python.backup_storages.BackupStorageClient,
) -> None:
    """Test successfully listing backup storages by project ID."""
    expected_api_resp = helpers.build_api_response(
        [simple_backup_storage, simple_backup_storage], 200
    )
    cast(
        mock.Mock, backup_storages_client._api_client.get
    ).return_value = expected_api_resp
    backup_storages = backup_storages_client.list_by_project(123456)

    for backup_storage, expected_backup_storage in zip(
        backup_storages, [simple_backup_storage, simple_backup_storage], strict=False
    ):
        assert (
            backup_storage.get_model()
            == cherryservers_sdk_python.backup_storages.BackupStorageModel.model_validate(
                expected_backup_storage
            )
        )

    cast(mock.Mock, backup_storages_client._api_client.get).assert_called_with(
        "projects/123456/backup-storages",
        {
            "fields": "available_addresses,ip,region,project,"
            "href,targeted_to,hostname,id,bgp,status,state,"
            "private_ip,public_ip,size_gigabytes,used_gigabytes,"
            "methods,rules,plan,pricing,name,"
            "whitelist,enabled,processing"
        },
        backup_storages_client.request_timeout,
    )


def test_list_backup_plans_success(
    simple_backup_storage_plan: dict[str, Any],
    backup_storages_client: cherryservers_sdk_python.backup_storages.BackupStorageClient,
) -> None:
    """Test successfully listing backup storage plans."""
    expected_api_resp = helpers.build_api_response(
        [simple_backup_storage_plan, simple_backup_storage_plan], 200
    )
    cast(
        mock.Mock, backup_storages_client._api_client.get
    ).return_value = expected_api_resp
    backup_storage_plan_models = backup_storages_client.list_backup_plans()

    for backup_storage_plan_model, expected_backup_storage_plan_model in zip(
        backup_storage_plan_models,
        [simple_backup_storage_plan, simple_backup_storage_plan],
        strict=False,
    ):
        assert (
            backup_storage_plan_model
            == cherryservers_sdk_python.backup_storages.BackupStoragePlanModel.model_validate(
                expected_backup_storage_plan_model
            )
        )

    cast(mock.Mock, backup_storages_client._api_client.get).assert_called_with(
        "backup-storage-plans",
        {"fields": "plan,pricing,href,region"},
        backup_storages_client.request_timeout,
    )


def test_create_success(
    backup_storages_client: cherryservers_sdk_python.backup_storages.BackupStorageClient,
    simple_backup_storage: dict[str, Any],
) -> None:
    """Test successfully creating a block storage."""
    creation_request = cherryservers_sdk_python.backup_storages.CreationRequest(
        region="LT-Siauliai", slug="backup_50"
    )

    undeployed_backup_storage = copy.deepcopy(simple_backup_storage)
    undeployed_backup_storage["status"] = "provisioning"

    get_response = helpers.build_api_response(simple_backup_storage, 200)
    post_response = helpers.build_api_response(undeployed_backup_storage, 201)
    cast(
        mock.Mock, backup_storages_client._api_client.post
    ).return_value = post_response
    cast(mock.Mock, backup_storages_client._api_client.get).return_value = get_response

    backup_storage = backup_storages_client.create(creation_request, 622690)

    assert (
        backup_storage.get_model()
        == cherryservers_sdk_python.backup_storages.BackupStorageModel.model_validate(
            simple_backup_storage
        )
    )

    cast(mock.Mock, backup_storages_client._api_client.post).assert_called_with(
        "servers/622690/backup-storages",
        creation_request,
        None,
        backup_storages_client.request_timeout,
    )

    cast(mock.Mock, backup_storages_client._api_client.get).assert_called_with(
        f"backup-storages/{simple_backup_storage['id']}",
        {
            "fields": "available_addresses,ip,region,project,"
            "href,targeted_to,hostname,id,bgp,status,state,"
            "private_ip,public_ip,size_gigabytes,used_gigabytes,"
            "methods,rules,plan,pricing,name,"
            "whitelist,enabled,processing"
        },
        backup_storages_client.request_timeout,
    )


def test_update_success(
    simple_backup_storage: dict[str, Any],
    backup_storages_client: cherryservers_sdk_python.backup_storages.BackupStorageClient,
) -> None:
    """Test successfully updating a backup storage."""
    update_req = cherryservers_sdk_python.backup_storages.UpdateRequest(
        slug="backup_50"
    )

    undeployed_backup_storage = copy.deepcopy(simple_backup_storage)
    undeployed_backup_storage["status"] = "provisioning"

    cast(
        mock.Mock, backup_storages_client._api_client.get
    ).return_value = helpers.build_api_response(simple_backup_storage, 200)
    cast(
        mock.Mock, backup_storages_client._api_client.put
    ).return_value = helpers.build_api_response(undeployed_backup_storage, 201)

    backup_storage = backup_storages_client.update(
        simple_backup_storage["id"], update_req
    )

    assert (
        backup_storage.get_model()
        == cherryservers_sdk_python.backup_storages.BackupStorageModel.model_validate(
            simple_backup_storage
        )
    )

    cast(mock.Mock, backup_storages_client._api_client.get).assert_called_with(
        f"backup-storages/{simple_backup_storage['id']}",
        {
            "fields": "available_addresses,ip,region,project,"
            "href,targeted_to,hostname,id,bgp,status,state,"
            "private_ip,public_ip,size_gigabytes,used_gigabytes,"
            "methods,rules,plan,pricing,name,"
            "whitelist,enabled,processing"
        },
        backup_storages_client.request_timeout,
    )

    cast(mock.Mock, backup_storages_client._api_client.put).assert_called_once_with(
        f"backup-storages/{simple_backup_storage['id']}",
        update_req,
        None,
        backup_storages_client._request_timeout,
    )


def test_update_access_method_success(
    simple_backup_storage: dict[str, Any],
    backup_storages_client: cherryservers_sdk_python.backup_storages.BackupStorageClient,
) -> None:
    """Test successfully updating a backup storages access method."""
    update_req = cherryservers_sdk_python.backup_storages.UpdateAccessMethodsRequest(
        enabled=True
    )

    cast(
        mock.Mock, backup_storages_client._api_client.get
    ).return_value = helpers.build_api_response(simple_backup_storage, 200)
    cast(
        mock.Mock, backup_storages_client._api_client.patch
    ).return_value = helpers.build_api_response(simple_backup_storage, 200)

    backup_storage = backup_storages_client.update_access_method(
        simple_backup_storage["id"], "ftp", update_req
    )

    assert (
        backup_storage.get_model()
        == cherryservers_sdk_python.backup_storages.BackupStorageModel.model_validate(
            simple_backup_storage
        )
    )

    cast(mock.Mock, backup_storages_client._api_client.get).assert_called_with(
        f"backup-storages/{simple_backup_storage['id']}",
        {
            "fields": "available_addresses,ip,region,project,"
            "href,targeted_to,hostname,id,bgp,status,state,"
            "private_ip,public_ip,size_gigabytes,used_gigabytes,"
            "methods,rules,plan,pricing,name,"
            "whitelist,enabled,processing"
        },
        backup_storages_client.request_timeout,
    )

    cast(mock.Mock, backup_storages_client._api_client.patch).assert_called_once_with(
        f"backup-storages/{simple_backup_storage['id']}/methods/ftp",
        update_req,
        None,
        backup_storages_client._request_timeout,
    )


def test_delete_success(
    simple_backup_storage: dict[str, Any],
    backup_storages_client: cherryservers_sdk_python.backup_storages.BackupStorageClient,
) -> None:
    """Test successfully deleting a block storage."""
    cast(
        mock.Mock, backup_storages_client._api_client.delete
    ).return_value = helpers.build_api_response({}, 204)

    backup_storages_client.delete(simple_backup_storage["id"])

    cast(mock.Mock, backup_storages_client._api_client.delete).assert_called_once_with(
        f"backup-storages/{simple_backup_storage['id']}",
        None,
        backup_storages_client._request_timeout,
    )

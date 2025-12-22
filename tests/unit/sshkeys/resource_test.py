"""Unit tests for Cherry Servers Python SDK SSH key resource."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, cast

import cherryservers_sdk_python.users
from tests.unit import helpers

if TYPE_CHECKING:
    from unittest import mock


def test_get_id(
    sshkey_resource: cherryservers_sdk_python.sshkeys.SSHKey,
) -> None:
    """Test getting SSH key resource ID."""
    assert sshkey_resource.get_id() == sshkey_resource.get_model().id


def test_update(
    sshkey_resource: cherryservers_sdk_python.sshkeys.SSHKey,
    simple_sshkey: dict[str, Any],
) -> None:
    """Test updating an SSH key resource."""
    update_req = cherryservers_sdk_python.sshkeys.UpdateRequest(
        label=simple_sshkey["label"],
        key=simple_sshkey["key"],
    )

    cast(
        "mock.Mock", sshkey_resource._client._api_client.get
    ).return_value = helpers.build_api_response(simple_sshkey, 200)
    cast(
        "mock.Mock", sshkey_resource._client._api_client.put
    ).return_value = helpers.build_api_response(simple_sshkey, 201)

    sshkey_resource.update(update_req)

    assert (
        sshkey_resource.get_model()
        == cherryservers_sdk_python.sshkeys.SSHKeyModel.model_validate(simple_sshkey)
    )

    cast("mock.Mock", sshkey_resource._client._api_client.get).assert_called_once_with(
        f"ssh-keys/{simple_sshkey['id']}",
        {"fields": "ssh_key,user"},
        sshkey_resource._client.request_timeout,
    )

    cast("mock.Mock", sshkey_resource._client._api_client.put).assert_called_once_with(
        f"ssh-keys/{simple_sshkey['id']}",
        update_req,
        None,
        sshkey_resource._client._request_timeout,
    )


def test_delete(
    sshkey_resource: cherryservers_sdk_python.sshkeys.SSHKey,
    simple_sshkey: dict[str, Any],
) -> None:
    """Test deleting an SSH key resource."""
    cast(
        "mock.Mock", sshkey_resource._client._api_client.delete
    ).return_value = helpers.build_api_response({}, 204)

    sshkey_resource.delete()

    cast(
        "mock.Mock", sshkey_resource._client._api_client.delete
    ).assert_called_once_with(
        f"ssh-keys/{simple_sshkey['id']}",
        None,
        sshkey_resource._client._request_timeout,
    )

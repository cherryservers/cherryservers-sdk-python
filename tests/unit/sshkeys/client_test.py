"""Unit tests for Cherry Servers Python SDK SSH keys client."""

from __future__ import annotations

from typing import Any, cast
from unittest import mock

import cherryservers_sdk_python.users
from tests.unit import helpers


def test_get_by_id_success(
    simple_sshkey: dict[str, Any],
    sshkeys_client: cherryservers_sdk_python.sshkeys.SSHKeyClient,
) -> None:
    """Test successfully getting SSH key by ID."""
    expected_api_resp = helpers.build_api_response(simple_sshkey, 200)
    cast(mock.Mock, sshkeys_client._api_client.get).return_value = expected_api_resp
    sshkey = sshkeys_client.get_by_id(simple_sshkey["id"])

    assert (
        sshkey.get_model()
        == cherryservers_sdk_python.sshkeys.SSHKeyModel.model_validate(simple_sshkey)
    )

    cast(mock.Mock, sshkeys_client._api_client.get).assert_called_with(
        f"ssh-keys/{simple_sshkey['id']}",
        {"fields": "ssh_key,user"},
        sshkeys_client.request_timeout,
    )


def test_get_all_success(
    simple_sshkey: dict[str, Any],
    sshkeys_client: cherryservers_sdk_python.sshkeys.SSHKeyClient,
) -> None:
    """Test successfully getting all SSH keys."""
    expected_api_resp = helpers.build_api_response([simple_sshkey, simple_sshkey], 200)
    cast(mock.Mock, sshkeys_client._api_client.get).return_value = expected_api_resp
    sshkeys = sshkeys_client.get_all()

    for sshkey, expected_sshkey in zip(
        sshkeys, [simple_sshkey, simple_sshkey], strict=False
    ):
        assert (
            sshkey.get_model()
            == cherryservers_sdk_python.sshkeys.SSHKeyModel.model_validate(
                expected_sshkey
            )
        )

    cast(mock.Mock, sshkeys_client._api_client.get).assert_called_with(
        "ssh-keys", {"fields": "ssh_key,user"}, sshkeys_client.request_timeout
    )


def test_create_success(
    simple_sshkey: dict[str, Any],
    sshkeys_client: cherryservers_sdk_python.sshkeys.SSHKeyClient,
) -> None:
    """Test successfully creating an SSH key."""
    creation_schema = cherryservers_sdk_python.sshkeys.CreationRequest(
        label=simple_sshkey["label"],
        key=simple_sshkey["key"],
    )

    get_response = helpers.build_api_response(simple_sshkey, 200)
    post_response = helpers.build_api_response(simple_sshkey, 201)
    cast(mock.Mock, sshkeys_client._api_client.post).return_value = post_response
    cast(mock.Mock, sshkeys_client._api_client.get).return_value = get_response

    sshkey = sshkeys_client.create(creation_schema)

    assert (
        sshkey.get_model()
        == cherryservers_sdk_python.sshkeys.SSHKeyModel.model_validate(simple_sshkey)
    )

    cast(mock.Mock, sshkeys_client._api_client.post).assert_called_with(
        "ssh-keys", creation_schema, None, sshkeys_client.request_timeout
    )

    cast(mock.Mock, sshkeys_client._api_client.get).assert_called_with(
        f"ssh-keys/{simple_sshkey['id']}",
        {"fields": "ssh_key,user"},
        sshkeys_client.request_timeout,
    )


def test_update_success(
    simple_sshkey: dict[str, Any],
    sshkeys_client: cherryservers_sdk_python.sshkeys.SSHKeyClient,
) -> None:
    """Test successfully updating an SSH key."""
    update_req = cherryservers_sdk_python.sshkeys.UpdateRequest(
        label=simple_sshkey["label"],
        key=simple_sshkey["key"],
    )

    cast(
        mock.Mock, sshkeys_client._api_client.get
    ).return_value = helpers.build_api_response(simple_sshkey, 200)
    cast(
        mock.Mock, sshkeys_client._api_client.put
    ).return_value = helpers.build_api_response(simple_sshkey, 201)

    sshkey = sshkeys_client.update(simple_sshkey["id"], update_req)

    assert (
        sshkey.get_model()
        == cherryservers_sdk_python.sshkeys.SSHKeyModel.model_validate(simple_sshkey)
    )

    cast(mock.Mock, sshkeys_client._api_client.get).assert_called_once_with(
        f"ssh-keys/{simple_sshkey['id']}",
        {"fields": "ssh_key,user"},
        sshkeys_client.request_timeout,
    )

    cast(mock.Mock, sshkeys_client._api_client.put).assert_called_once_with(
        f"ssh-keys/{simple_sshkey['id']}",
        update_req,
        None,
        sshkeys_client._request_timeout,
    )


def test_delete_success(
    simple_sshkey: dict[str, Any],
    sshkeys_client: cherryservers_sdk_python.sshkeys.SSHKeyClient,
) -> None:
    """Test successfully deleting an SSH key."""
    cast(
        mock.Mock, sshkeys_client._api_client.delete
    ).return_value = helpers.build_api_response({}, 204)

    sshkeys_client.delete(simple_sshkey["id"])

    cast(mock.Mock, sshkeys_client._api_client.delete).assert_called_once_with(
        f"ssh-keys/{simple_sshkey['id']}", None, sshkeys_client._request_timeout
    )

"""Unit tests for Cherry Servers Python SDK server resource."""

from __future__ import annotations

import copy
from operator import methodcaller
from typing import Any, cast
from unittest import mock

import pytest

import cherryservers_sdk_python.users
from cherryservers_sdk_python import _base
from tests.unit import helpers


def test_get_id(
    server_resource: cherryservers_sdk_python.servers.Server,
) -> None:
    """Test getting server resource ID."""
    assert server_resource.get_id() == server_resource.get_model().id


def test_update(
    server_resource: cherryservers_sdk_python.servers.Server,
    simple_server: dict[str, Any],
) -> None:
    """Test updating a server resource."""
    update_req = cherryservers_sdk_python.servers.UpdateRequest(
        name="updated-server-name",
        hostname="updated-server-hostname",
        tags={"updated-tag": "updated-value"},
        bgp=True,
    )
    updated_server = copy.deepcopy(simple_server)
    updated_server["name"] = update_req.name
    updated_server["hostname"] = update_req.hostname
    updated_server["tags"] = update_req.tags
    updated_server["bgp"]["enabled"] = update_req.bgp

    cast(
        mock.Mock, server_resource._client._api_client.get
    ).return_value = helpers.build_api_response(updated_server, 200)
    cast(
        mock.Mock, server_resource._client._api_client.put
    ).return_value = helpers.build_api_response(updated_server, 201)

    server_resource.update(update_req)

    assert (
        server_resource.get_model()
        == cherryservers_sdk_python.servers.ServerModel.model_validate(updated_server)
    )

    cast(mock.Mock, server_resource._client._api_client.get).assert_called_once_with(
        f"servers/{simple_server['id']}", None, server_resource._client._request_timeout
    )

    cast(mock.Mock, server_resource._client._api_client.put).assert_called_once_with(
        f"servers/{simple_server['id']}",
        update_req,
        None,
        server_resource._client._request_timeout,
    )


def test_delete(
    server_resource: cherryservers_sdk_python.servers.Server,
    simple_server: dict[str, Any],
) -> None:
    """Test deleting a server resource."""
    cast(
        mock.Mock, server_resource._client._api_client.delete
    ).return_value = helpers.build_api_response({}, 204)

    server_resource.delete()

    cast(mock.Mock, server_resource._client._api_client.delete).assert_called_once_with(
        f"servers/{simple_server['id']}", None, server_resource._client._request_timeout
    )


@pytest.mark.parametrize(
    ("in_progress_status", "action_func_name", "action_request"),
    [
        (
            "powering_off",
            "power_off",
            cherryservers_sdk_python.servers.PowerOffRequest(),
        ),
        (
            "powering_on",
            "power_on",
            cherryservers_sdk_python.servers.PowerOnRequest(),
        ),
        (
            "powering_on",
            "reboot",
            cherryservers_sdk_python.servers.RebootRequest(),
        ),
        (
            "entering rescue mode",
            "enter_rescue_mode",
            cherryservers_sdk_python.servers.EnterRescueModeRequest(
                password="123456789"  # noqa: S106
            ),
        ),
        (
            "exiting rescue mode",
            "exit_rescue_mode",
            cherryservers_sdk_python.servers.ExitRescueModeRequest(),
        ),
        (
            "powering_on",
            "rebuild",
            cherryservers_sdk_python.servers.RebuildRequest(
                image="fedora_41_64bit",
                hostname="test",
                password="123456789",  # noqa: S106
                ssh_keys=set(),
                user_data="abc",
            ),
        ),
        (
            "deployed",
            "reset_bmc_password",
            cherryservers_sdk_python.servers.ResetBMCPasswordRequest(),
        ),
    ],
)
def test_actions(
    server_resource: cherryservers_sdk_python.servers.Server,
    simple_server: dict[str, Any],
    in_progress_status: str,
    action_func_name: str,
    action_request: _base.RequestSchema,
) -> None:
    """Test server actions."""
    simple_server["plan"]["type"] = "baremetal"
    server_with_action_in_progress = copy.deepcopy(simple_server)
    server_with_action_in_progress["status"] = in_progress_status

    if action_func_name == "enter_rescue_mode":
        method_to_test = methodcaller(action_func_name, action_request)
        simple_server["status"] = "rescue mode"
    elif action_func_name == "rebuild":
        method_to_test = methodcaller(action_func_name, action_request)
    else:
        method_to_test = methodcaller(action_func_name)

    cast(
        mock.Mock, server_resource._client._api_client.post
    ).return_value = helpers.build_api_response(server_with_action_in_progress, 201)
    cast(
        mock.Mock, server_resource._client._api_client.get
    ).return_value = helpers.build_api_response(simple_server, 200)

    method_to_test(server_resource)

    cast(mock.Mock, server_resource._client._api_client.get).assert_called_with(
        f"servers/{simple_server['id']}", None, server_resource._client._request_timeout
    )

    cast(mock.Mock, server_resource._client._api_client.post).assert_called_with(
        f"servers/{simple_server['id']}/actions",
        action_request,
        None,
        server_resource._client._request_timeout,
    )

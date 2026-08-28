"""Unit tests for Cherry Servers Python SDK server client."""

from __future__ import annotations

import copy
from operator import methodcaller
from typing import TYPE_CHECKING, Any, cast

import pytest

import cherryservers_sdk_python
from cherryservers_sdk_python import _base
from tests.unit import helpers

if TYPE_CHECKING:
    from unittest import mock

    from cherryservers_sdk_python._client import CherryApiClient


def test_get_by_id_success(
    simple_server: dict[str, Any],
    servers_client: cherryservers_sdk_python.servers.ServerClient,
) -> None:
    """Test successfully getting server by ID."""
    expected_api_resp = helpers.build_api_response(simple_server, 200)
    cast("mock.Mock", servers_client._api_client.get).return_value = expected_api_resp
    server = servers_client.get_by_id(simple_server["id"])

    assert (
        server.get_model()
        == cherryservers_sdk_python.servers.ServerModel.model_validate(simple_server)
    )

    cast("mock.Mock", servers_client._api_client.get).assert_called_with(
        f"servers/{simple_server['id']}",
        None,
        servers_client.request_timeout,
    )


def test_list_by_project_success(
    simple_server: dict[str, Any],
    servers_client: cherryservers_sdk_python.servers.ServerClient,
) -> None:
    """Test successfully getting servers by project."""
    expected_api_resp = helpers.build_api_response([simple_server, simple_server], 200)
    cast("mock.Mock", servers_client._api_client.get).return_value = expected_api_resp
    servers = servers_client.list_by_project(simple_server["project"]["id"])

    for server, expected_server in zip(
        servers, [simple_server, simple_server], strict=False
    ):
        assert (
            server.get_model()
            == cherryservers_sdk_python.servers.ServerModel.model_validate(
                expected_server
            )
        )

    cast("mock.Mock", servers_client._api_client.get).assert_called_with(
        f"projects/{simple_server['project']['id']}/servers",
        None,
        servers_client.request_timeout,
    )


@pytest.mark.parametrize(
    "creation_request",
    [
        cherryservers_sdk_python.servers.CreationRequest(
            plan="amd-ryzen-9700x",
            image="fedora_41_64bit",
            region="LT-Siauliai",
        ),
        cherryservers_sdk_python.servers.CreationRequest(
            plan="amd-ryzen-9700x",
            image="ubuntu_24_04_64bit",
            region="LT-Siauliai",
            hostname="test",
            ssh_keys=set(),
            ip_addresses=set(),
            user_data="abc",
            tags={},
            spot_market=False,
            storage_id=0,
        ),
        cherryservers_sdk_python.servers.CreationRequest(
            plan="amd-ryzen-9700x",
            image="custom_ipxe_install",
            region="LT-Siauliai",
            ipxe="abc",
        ),
    ],
)
def test_create_success(
    simple_server: dict[str, Any],
    servers_client: cherryservers_sdk_python.servers.ServerClient,
    creation_request: cherryservers_sdk_python.servers.CreationRequest,
) -> None:
    """Test successfully creating a server."""
    server_pre_deploy = copy.deepcopy(simple_server)
    server_pre_deploy["status"] = "deploying"

    get_response = helpers.build_api_response(simple_server, 200)
    post_response = helpers.build_api_response(server_pre_deploy, 201)
    cast("mock.Mock", servers_client._api_client.post).return_value = post_response
    cast("mock.Mock", servers_client._api_client.get).return_value = get_response

    server = servers_client.create(creation_request, simple_server["project"]["id"])

    assert (
        server.get_model()
        == cherryservers_sdk_python.servers.ServerModel.model_validate(simple_server)
    )

    cast("mock.Mock", servers_client._api_client.post).assert_called_with(
        f"projects/{simple_server['project']['id']}/servers",
        creation_request,
        None,
        servers_client.request_timeout,
    )

    cast("mock.Mock", servers_client._api_client.get).assert_called_with(
        f"servers/{simple_server['id']}",
        None,
        servers_client.request_timeout,
    )


def test_update_success(
    simple_server: dict[str, Any],
    servers_client: cherryservers_sdk_python.servers.ServerClient,
) -> None:
    """Test successfully updating a server."""
    update_req = cherryservers_sdk_python.servers.UpdateRequest(
        name="test-updated",
        hostname="test-updated",
        tags={"test": "test-updated"},
        bgp=True,
    )
    updated_server = copy.deepcopy(simple_server)
    updated_server["name"] = update_req.name
    updated_server["hostname"] = update_req.hostname
    updated_server["tags"] = update_req.tags
    updated_server["bgp"]["enabled"] = update_req.bgp

    get_response = helpers.build_api_response(updated_server, 200)
    put_response = helpers.build_api_response(updated_server, 201)
    cast("mock.Mock", servers_client._api_client.put).return_value = put_response
    cast("mock.Mock", servers_client._api_client.get).return_value = get_response

    server = servers_client.update(simple_server["id"], update_req)

    assert (
        server.get_model()
        == cherryservers_sdk_python.servers.ServerModel.model_validate(updated_server)
    )

    cast("mock.Mock", servers_client._api_client.put).assert_called_with(
        f"servers/{simple_server['id']}",
        update_req,
        None,
        servers_client.request_timeout,
    )

    cast("mock.Mock", servers_client._api_client.get).assert_called_with(
        f"servers/{simple_server['id']}",
        None,
        servers_client.request_timeout,
    )


def test_delete_success(
    simple_server: dict[str, Any],
    servers_client: cherryservers_sdk_python.servers.ServerClient,
) -> None:
    """Test successfully deleting a server."""
    cast(
        "mock.Mock", servers_client._api_client.delete
    ).return_value = helpers.build_api_response({}, 204)

    servers_client.delete(simple_server["id"])

    cast("mock.Mock", servers_client._api_client.delete).assert_called_once_with(
        f"servers/{simple_server['id']}", None, servers_client._request_timeout
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
                image="ubuntu_24_04_64bit",
                hostname="test",
                password="123456789",  # noqa: S106
                ssh_keys=set(),
                user_data="abc",
                ipxe="abc",
                persist_ipxe=True,
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
    simple_server: dict[str, Any],
    servers_client: cherryservers_sdk_python.servers.ServerClient,
    in_progress_status: str,
    action_func_name: str,
    action_request: _base.RequestSchema,
) -> None:
    """Test server actions."""
    simple_server["plan"]["type"] = "baremetal"
    server_with_action_in_progress = copy.deepcopy(simple_server)
    server_with_action_in_progress["status"] = in_progress_status

    if action_func_name == "enter_rescue_mode":
        method_to_test = methodcaller(
            action_func_name, simple_server["id"], action_request
        )
        simple_server["status"] = "rescue mode"
    elif action_func_name == "rebuild":
        method_to_test = methodcaller(
            action_func_name, simple_server["id"], action_request
        )
    else:
        method_to_test = methodcaller(action_func_name, simple_server["id"])

    cast(
        "mock.Mock", servers_client._api_client.post
    ).return_value = helpers.build_api_response(server_with_action_in_progress, 201)
    cast(
        "mock.Mock", servers_client._api_client.get
    ).return_value = helpers.build_api_response(simple_server, 200)

    method_to_test(servers_client)

    cast("mock.Mock", servers_client._api_client.get).assert_called_with(
        f"servers/{simple_server['id']}", None, servers_client.request_timeout
    )

    cast("mock.Mock", servers_client._api_client.post).assert_called_with(
        f"servers/{simple_server['id']}/actions",
        action_request,
        None,
        servers_client.request_timeout,
    )


def _setup_failed_deployment(
    resp_body_ok: dict[str, Any], mock_client: CherryApiClient
) -> None:
    resp_body_ok["status"] = "deploying"
    resp_body_failed = copy.deepcopy(resp_body_ok)
    resp_body_failed["status"] = "failed deployment"

    get_fail_resp = helpers.build_api_response(resp_body_failed, 200)
    post_ok_resp = helpers.build_api_response(resp_body_ok, 201)
    put_ok_resp = post_ok_resp
    cast("mock.Mock", mock_client.get).return_value = get_fail_resp
    cast("mock.Mock", mock_client.post).return_value = post_ok_resp
    cast("mock.Mock", mock_client.put).return_value = put_ok_resp


def test_deployment_error_propagation(
    subtests: pytest.Subtests,
    simple_server: dict[str, Any],
    servers_client: cherryservers_sdk_python.servers.ServerClient,
) -> None:
    """Test server deployment failure error propagation."""
    simple_server["plan"]["type"] = "baremetal"
    _setup_failed_deployment(simple_server, servers_client._api_client)

    with (
        subtests.test("create"),
        pytest.raises(cherryservers_sdk_python.servers.FailedDeploymentError),
    ):
        servers_client.create(
            cherryservers_sdk_python.servers.CreationRequest(
                plan="test-plan",
                region="test-region",
            ),
            simple_server["project"]["id"],
        )

    with (
        subtests.test("power off"),
        pytest.raises(cherryservers_sdk_python.servers.FailedDeploymentError),
    ):
        servers_client.power_off(
            simple_server["project"]["id"],
        )

    with (
        subtests.test("power on"),
        pytest.raises(cherryservers_sdk_python.servers.FailedDeploymentError),
    ):
        servers_client.power_on(
            simple_server["project"]["id"],
        )

    with (
        subtests.test("reboot"),
        pytest.raises(cherryservers_sdk_python.servers.FailedDeploymentError),
    ):
        servers_client.reboot(
            simple_server["project"]["id"],
        )

    with (
        subtests.test("power off"),
        pytest.raises(cherryservers_sdk_python.servers.FailedDeploymentError),
    ):
        servers_client.power_off(
            simple_server["project"]["id"],
        )

    with (
        subtests.test("enter rescue mode"),
        pytest.raises(cherryservers_sdk_python.servers.FailedDeploymentError),
    ):
        servers_client.enter_rescue_mode(
            simple_server["project"]["id"],
            cherryservers_sdk_python.servers.EnterRescueModeRequest(
                password="test",  # noqa: S106
            ),
        )

    with (
        subtests.test("exit rescue mode"),
        pytest.raises(cherryservers_sdk_python.servers.FailedDeploymentError),
    ):
        servers_client.exit_rescue_mode(
            simple_server["project"]["id"],
        )

    with (
        subtests.test("rebuilt"),
        pytest.raises(cherryservers_sdk_python.servers.FailedDeploymentError),
    ):
        servers_client.rebuild(
            simple_server["project"]["id"],
            cherryservers_sdk_python.servers.RebuildRequest(
                image="test-image",
                hostname="test-hostname",
                password="test",  # noqa: S106
            ),
        )

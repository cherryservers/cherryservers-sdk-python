"""Unit tests for Cherry Servers Python SDK IPs client."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, cast
from unittest import mock

import pytest

import cherryservers_sdk_python.ips
from tests.unit import helpers

if TYPE_CHECKING:
    from _pytest.fixtures import FixtureRequest


def test_get_by_id_success(
    simple_ip: dict[str, Any],
    ips_client: cherryservers_sdk_python.ips.IPClient,
) -> None:
    """Test successfully getting an IP by ID."""
    expected_api_resp = helpers.build_api_response(simple_ip, 200)
    cast(mock.Mock, ips_client._api_client.get).return_value = expected_api_resp
    project = ips_client.get_by_id(simple_ip["id"])

    assert project.get_model() == cherryservers_sdk_python.ips.IPModel.model_validate(
        simple_ip
    )

    cast(mock.Mock, ips_client._api_client.get).assert_called_with(
        f"ips/{simple_ip['id']}",
        {"fields": "ip,project,routed_to,region,href,bgp,id,hostname"},
        ips_client.request_timeout,
    )


def test_list_by_team_success(
    simple_ip: dict[str, Any],
    ips_client: cherryservers_sdk_python.ips.IPClient,
) -> None:
    """Test successfully listing all team projects."""
    expected_api_resp = helpers.build_api_response([simple_ip, simple_ip], 200)
    cast(mock.Mock, ips_client._api_client.get).return_value = expected_api_resp
    ips = ips_client.list_by_project(123456)

    for ip, expected_ip in zip(ips, [simple_ip, simple_ip]):
        assert ip.get_model() == cherryservers_sdk_python.ips.IPModel.model_validate(
            expected_ip
        )

    cast(mock.Mock, ips_client._api_client.get).assert_called_with(
        "projects/123456/ips",
        {"fields": "ip,project,routed_to,region,href,bgp,id,hostname"},
        ips_client.request_timeout,
    )


@pytest.mark.parametrize(
    ("creation_request", "ip_fixture_name"),
    [
        (cherryservers_sdk_python.ips.CreationRequest(region="eu_nord_1"), "simple_ip"),
        (
            cherryservers_sdk_python.ips.CreationRequest(
                region="eu_nord_1",
                targeted_to=123456,
                ptr_record="test",
                a_record="test",
                tags={"env": "test"},
            ),
            "attached_ip",
        ),
    ],
)
def test_create_success(
    ip_fixture_name: str,
    creation_request: cherryservers_sdk_python.ips.CreationRequest,
    ips_client: cherryservers_sdk_python.ips.IPClient,
    request: FixtureRequest,
) -> None:
    """Test successfully creating an IP."""
    ip = request.getfixturevalue(ip_fixture_name)

    get_response = helpers.build_api_response(ip, 200)
    post_response = helpers.build_api_response(ip, 201)
    cast(mock.Mock, ips_client._api_client.post).return_value = post_response
    cast(mock.Mock, ips_client._api_client.get).return_value = get_response

    project = ips_client.create(creation_request, 123456)

    assert project.get_model() == cherryservers_sdk_python.ips.IPModel.model_validate(
        ip
    )

    cast(mock.Mock, ips_client._api_client.post).assert_called_with(
        "projects/123456/ips", creation_request, None, ips_client.request_timeout
    )

    cast(mock.Mock, ips_client._api_client.get).assert_called_with(
        f"ips/{ip['id']}",
        {"fields": "ip,project,routed_to,region,href,bgp,id,hostname"},
        ips_client.request_timeout,
    )


def test_update_success(
    attached_ip: dict[str, Any],
    ips_client: cherryservers_sdk_python.ips.IPClient,
) -> None:
    """Test successfully updating an IP."""
    update_req = cherryservers_sdk_python.ips.UpdateRequest(
        targeted_to=123456,
        ptr_record="test",
        a_record="test",
        tags={"env": "test"},
    )

    cast(
        mock.Mock, ips_client._api_client.get
    ).return_value = helpers.build_api_response(attached_ip, 200)
    cast(
        mock.Mock, ips_client._api_client.put
    ).return_value = helpers.build_api_response(attached_ip, 201)

    ip = ips_client.update(attached_ip["id"], update_req)

    assert ip.get_model() == cherryservers_sdk_python.ips.IPModel.model_validate(
        attached_ip
    )

    cast(mock.Mock, ips_client._api_client.get).assert_called_with(
        f"ips/{attached_ip['id']}",
        {"fields": "ip,project,routed_to,region,href,bgp,id,hostname"},
        ips_client.request_timeout,
    )

    cast(mock.Mock, ips_client._api_client.put).assert_called_once_with(
        f"ips/{attached_ip['id']}",
        update_req,
        None,
        ips_client._request_timeout,
    )


def test_delete_success(
    simple_ip: dict[str, Any],
    ips_client: cherryservers_sdk_python.ips.IPClient,
) -> None:
    """Test successfully deleting an IP."""
    cast(
        mock.Mock, ips_client._api_client.delete
    ).return_value = helpers.build_api_response({}, 204)

    ips_client.delete(simple_ip["id"])

    cast(mock.Mock, ips_client._api_client.delete).assert_called_once_with(
        f"ips/{simple_ip['id']}", None, ips_client._request_timeout
    )

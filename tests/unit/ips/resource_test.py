"""Unit tests for Cherry Servers Python SDK IP resource."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, cast

import cherryservers_sdk_python.ips
from tests.unit import helpers

if TYPE_CHECKING:
    from unittest import mock


def test_get_id(
    ip_resource: cherryservers_sdk_python.ips.IP,
) -> None:
    """Test getting IP resource ID."""
    assert ip_resource.get_id() == ip_resource.get_model().id


def test_update(
    ip_resource: cherryservers_sdk_python.ips.IP,
    attached_ip: dict[str, Any],
) -> None:
    """Test updating an IP resource."""
    update_req = cherryservers_sdk_python.ips.UpdateRequest(
        targeted_to=123456,
        ptr_record="test",
        a_record="test",
        tags={"env": "test"},
    )

    cast(
        "mock.Mock", ip_resource._client._api_client.get
    ).return_value = helpers.build_api_response(attached_ip, 200)
    cast(
        "mock.Mock", ip_resource._client._api_client.put
    ).return_value = helpers.build_api_response(attached_ip, 201)

    ip_resource.update(update_req)

    assert (
        ip_resource.get_model()
        == cherryservers_sdk_python.ips.IPModel.model_validate(attached_ip)
    )

    cast("mock.Mock", ip_resource._client._api_client.get).assert_called_once_with(
        f"ips/{attached_ip['id']}",
        {"fields": "ip,project,routed_to,region,href,bgp,id,hostname"},
        ip_resource._client.request_timeout,
    )

    cast("mock.Mock", ip_resource._client._api_client.put).assert_called_once_with(
        f"ips/{attached_ip['id']}",
        update_req,
        None,
        ip_resource._client._request_timeout,
    )


def test_delete(
    ip_resource: cherryservers_sdk_python.ips.IP,
    simple_ip: dict[str, Any],
) -> None:
    """Test deleting an IP resource."""
    cast(
        "mock.Mock", ip_resource._client._api_client.delete
    ).return_value = helpers.build_api_response({}, 204)

    ip_resource.delete()

    cast("mock.Mock", ip_resource._client._api_client.delete).assert_called_once_with(
        f"ips/{simple_ip['id']}",
        None,
        ip_resource._client._request_timeout,
    )

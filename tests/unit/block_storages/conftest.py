"""Cherry Servers Python SDK IPs unit test fixtures."""

from __future__ import annotations

from typing import Any
from unittest import mock

import pytest

import cherryservers_sdk_python


@pytest.fixture
def block_storages_client() -> (
    cherryservers_sdk_python.block_storages.BlockStorageClient
):
    """Initialize block storage client fixture."""
    return cherryservers_sdk_python.block_storages.BlockStorageClient(
        api_client=mock.MagicMock()
    )


@pytest.fixture
def block_storage_resource(
    simple_block_storage: dict[str, Any],
    block_storages_client: cherryservers_sdk_python.block_storages.BlockStorageClient,
) -> cherryservers_sdk_python.block_storages.BlockStorage:
    """Initialize block storage resource fixture."""
    return cherryservers_sdk_python.block_storages.BlockStorage(
        client=block_storages_client,
        model=cherryservers_sdk_python.block_storages.BlockStorageModel.model_validate(
            simple_block_storage
        ),
    )


@pytest.fixture
def simple_block_storage() -> dict[str, Any]:
    """Initialize simple block storage fixture."""
    return {
        "id": 622703,
        "name": "cs-volume-220189-622703",
        "href": "/storage/622703",
        "region": {
            "id": 1,
            "name": "EU-Nord-1",
            "slug": "eu_nord_1",
            "region_iso_2": "LT",
            "href": "/regions/1",
            "bgp": {"hosts": ["123.123.123.123", "123.123.123.123"], "asn": 12345},
            "location": "Lithuania, Šiauliai",
        },
        "size": 1,
        "allow_edit_size": False,
        "unit": "GB",
        "description": "",
    }


@pytest.fixture
def attached_block_storage() -> dict[str, Any]:
    """Initialize attached block storage fixture."""
    return {
        "id": 622703,
        "name": "cs-volume-220189-622703",
        "href": "/storage/622703",
        "region": {
            "id": 1,
            "name": "EU-Nord-1",
            "slug": "eu_nord_1",
            "region_iso_2": "LT",
            "href": "/regions/1",
            "bgp": {"hosts": ["123.123.123.123", "123.123.123.123"], "asn": 12345},
            "location": "Lithuania, Šiauliai",
        },
        "size": 1,
        "allow_edit_size": True,
        "unit": "GB",
        "description": "",
        "attached_to": {
            "id": 622711,
            "href": "/servers/622711",
            "hostname": "huge-quail",
            "region": {
                "id": 1,
                "name": "EU-Nord-1",
                "slug": "eu_nord_1",
                "region_iso_2": "LT",
                "href": "/regions/1",
                "bgp": {"hosts": ["123.123.123.123", "123.123.123.123"], "asn": 12345},
                "location": "Lithuania, Šiauliai",
            },
            "storage": {
                "id": 622703,
                "name": "cs-volume-220189-622703",
                "href": "/storage/622703",
                "region": {
                    "id": 1,
                    "name": "EU-Nord-1",
                    "slug": "eu_nord_1",
                    "region_iso_2": "LT",
                    "href": "/regions/1",
                    "bgp": {
                        "hosts": ["123.123.123.123", "123.123.123.123"],
                        "asn": 12345,
                    },
                    "location": "Lithuania, Šiauliai",
                },
                "size": 1,
                "allow_edit_size": True,
                "unit": "GB",
                "description": "",
                "attached_to": {
                    "id": 622711,
                    "href": "/servers/622711",
                    "hostname": "huge-quail",
                },
                "vlan_id": "1234",
                "vlan_ip": "123.123.123.123",
                "initiator": "iqn.2019-0...2211",
                "discovery_ip": "123.123.123.123",
            },
        },
        "vlan_id": "1234",
        "vlan_ip": "123.123.123.123",
        "initiator": "iqn.2019-0...2211",
        "discovery_ip": "123.123.123.123",
    }

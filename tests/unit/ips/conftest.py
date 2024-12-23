"""Cherry Servers Python SDK IPs unit test fixtures."""

from __future__ import annotations

from typing import Any
from unittest import mock

import pytest

import cherryservers_sdk_python.ips


@pytest.fixture
def ips_client() -> cherryservers_sdk_python.ips.IPClient:
    """Initialize IP client fixture."""
    return cherryservers_sdk_python.ips.IPClient(api_client=mock.MagicMock())


@pytest.fixture
def ip_resource(
    simple_ip: dict[str, Any],
    ips_client: cherryservers_sdk_python.ips.IPClient,
) -> cherryservers_sdk_python.ips.IP:
    """Initialize IP resource fixture."""
    return cherryservers_sdk_python.ips.IP(
        client=ips_client,
        model=cherryservers_sdk_python.ips.IPModel.model_validate(simple_ip),
    )


@pytest.fixture
def simple_ip() -> dict[str, Any]:
    """Initialize simple IP fixture."""
    return {
        "id": "bab8f4a1-07...0dfdc87ba",
        "address": "123.123.123.123",
        "address_family": 4,
        "cidr": "123.123.123.123/32",
        "type": "floating-ip",
        "region": {
            "id": 1,
            "name": "EU-Nord-1",
            "slug": "eu_nord_1",
            "region_iso_2": "LT",
            "href": "/regions/1",
            "bgp": {"hosts": ["123.123.123.123", "123.123.123.123"], "asn": 12345},
            "location": "Lithuania, Šiauliai",
        },
        "ddos_scrubbing": False,
        "tags": {},
        "project": {
            "id": 123456,
            "name": "cherryctl",
            "bgp": {"enabled": False, "local_asn": 0},
            "href": "/projects/123456",
        },
        "href": "/ips/bab8f4a1-07...0dfdc87ba",
    }


@pytest.fixture
def attached_ip() -> dict[str, Any]:
    """Initialize attached IP fixture."""
    return {
        "id": "bab8f4a1-07...0dfdc87ba",
        "address": "123.123.123.123",
        "address_family": 4,
        "cidr": "123.123.123.123/32",
        "type": "floating-ip",
        "region": {
            "id": 1,
            "name": "EU-Nord-1",
            "slug": "eu_nord_1",
            "region_iso_2": "LT",
            "href": "/regions/1",
            "bgp": {"hosts": ["123.123.123.123", "123.123.123.123"], "asn": 12345},
            "location": "Lithuania, Šiauliai",
        },
        "routed_to": {
            "id": "bab8f4a1-07...0dfdc87ba",
            "address": "123.123.123.123",
            "address_family": 4,
            "cidr": "123.123.123.123/24",
            "type": "primary-ip",
            "region": {
                "id": 1,
                "name": "EU-Nord-1",
                "slug": "eu_nord_1",
                "region_iso_2": "LT",
                "href": "/regions/1",
                "bgp": {"hosts": ["123.123.123.123", "123.123.123.123"], "asn": 12345},
                "location": "Lithuania, Šiauliai",
            },
            "assigned_to": {
                "id": 622690,
                "href": "/servers/622690",
                "hostname": "trusted-panda",
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
                "project": {
                    "id": 123456,
                    "name": "cherryctl",
                    "bgp": {"enabled": False, "local_asn": 0},
                    "href": "/projects/123456",
                },
            },
            "ddos_scrubbing": False,
            "tags": {},
            "project": {
                "id": 123456,
                "name": "cherryctl",
                "bgp": {"enabled": False, "local_asn": 0},
                "href": "/projects/123456",
            },
            "targeted_to": {
                "id": 622690,
                "href": "/servers/622690",
                "hostname": "trusted-panda",
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
                "project": {
                    "id": 123456,
                    "name": "cherryctl",
                    "bgp": {"enabled": False, "local_asn": 0},
                    "href": "/projects/123456",
                },
            },
            "href": "/ips/bab8f4a1-07...0dfdc87ba",
        },
        "ptr_record": "test.",
        "a_record": "test.cloud.cherryservers.net.",
        "ddos_scrubbing": False,
        "tags": {"env": "test"},
        "project": {
            "id": 123456,
            "name": "cherryctl",
            "bgp": {"enabled": False, "local_asn": 0},
            "href": "/projects/123456",
        },
        "targeted_to": {
            "id": 622690,
            "href": "/servers/622690",
            "hostname": "trusted-panda",
            "region": {
                "id": 1,
                "name": "EU-Nord-1",
                "slug": "eu_nord_1",
                "region_iso_2": "LT",
                "href": "/regions/1",
                "bgp": {"hosts": ["123.123.123.123", "123.123.123.123"], "asn": 12345},
                "location": "Lithuania, Šiauliai",
            },
            "bgp": {
                "enabled": False,
                "available": False,
                "status": "Disabled",
                "routers": 0,
                "connected": 0,
                "limit": 0,
                "active": 0,
                "routes": [],
                "updated": "2024-12-23T11:00:19+00:00",
            },
            "project": {
                "id": 123456,
                "name": "cherryctl",
                "bgp": {"enabled": False, "local_asn": 0},
                "href": "/projects/123456",
            },
        },
        "href": "/ips/bab8f4a1-07...0dfdc87ba",
    }

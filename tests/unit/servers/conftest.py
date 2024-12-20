"""Cherry Servers Python SDK server unit test fixtures."""

from __future__ import annotations

from typing import Any
from unittest import mock

import pytest

import cherryservers_sdk_python


@pytest.fixture
def servers_client() -> cherryservers_sdk_python.servers.ServerClient:
    """Initialize server client fixture."""
    return cherryservers_sdk_python.servers.ServerClient(api_client=mock.MagicMock())


@pytest.fixture
def server_resource(
    simple_server: dict[str, Any],
    servers_client: cherryservers_sdk_python.servers.ServerClient,
) -> cherryservers_sdk_python.servers.Server:
    """Initialize Server resource fixture."""
    return cherryservers_sdk_python.servers.Server(
        client=servers_client,
        model=cherryservers_sdk_python.servers.ServerModel.model_validate(
            simple_server
        ),
    )


@pytest.fixture
def simple_server() -> dict[str, Any]:
    """Initialize simple server fixture."""
    return {
        "id": 621229,
        "name": "Cloud VPS 1",
        "href": "/servers/621229",
        "hostname": "test",
        "password": "123456789",
        "username": "root",
        "image": "Fedora 41 64bit",
        "spot_instance": False,
        "region": {
            "id": 1,
            "name": "EU-Nord-1",
            "slug": "eu_nord_1",
            "region_iso_2": "LT",
            "href": "/regions/1",
            "bgp": {"hosts": ["123.123.123.123", "123.123.123.123"], "asn": 12345},
            "location": "Lithuania, Šiauliai",
        },
        "state": "active",
        "status": "deployed",
        "bgp": {
            "enabled": False,
            "available": False,
            "status": "Disabled",
            "routers": 0,
            "connected": 0,
            "limit": 0,
            "active": 0,
            "routes": [],
            "updated": "2024-12-18T12:30:23+00:00",
        },
        "software": {"addons": []},
        "plan": {
            "id": 625,
            "href": "/plans/cloud_vps_1",
            "name": "Cloud VPS 1",
            "slug": "cloud_vps_1",
            "title": "Cloud VPS 1",
            "type": "vps",
            "category": "Shared resources",
            "specs": {
                "cpus": {
                    "count": 1,
                    "name": "1 vCore",
                    "cores": 1,
                    "frequency": 0.0,
                    "unit": "GHz",
                },
                "memory": {"count": 1, "total": 1, "unit": "GB", "name": "1GB"},
                "storage": [
                    {
                        "count": 1,
                        "name": "SSD 20GB",
                        "size": 20,
                        "unit": "GB",
                        "type": "SSD",
                    }
                ],
                "nics": {"name": "1Gbps"},
                "bandwidth": {"name": "1TB"},
            },
            "pricing": [
                {
                    "id": 37,
                    "unit": "Hourly",
                    "price": 0.0182,
                    "currency": "USD",
                    "taxed": False,
                }
            ],
        },
        "pricing": {
            "id": 37,
            "currency": "EUR",
            "unit": "Hours",
            "unit_price": 0.01815,
            "discount": 0.0,
            "discount_percentage": False,
            "price_subtotal": 0.060000000000000005,
            "taxed": True,
            "price_total": 0.0726,
            "price": 0.0726,
            "quantity": 4,
            "billable_amount": 0.0726,
        },
        "ip_addresses": [
            {
                "id": "1decf524...22ce24df8de",
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
                    "bgp": {
                        "hosts": ["123.123.123.123", "123.123.123.123"],
                        "asn": 12345,
                    },
                    "location": "Lithuania, Šiauliai",
                },
                "assigned_to": {
                    "id": 621229,
                    "name": "Cloud VPS 1",
                    "href": "/servers/621229",
                    "hostname": "test",
                    "password": "123456789",
                    "username": "root",
                    "spot_instance": False,
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
                    "state": "active",
                    "software": {"addons": []},
                    "tags": {},
                    "termination_date": "None",
                    "upgradable": False,
                    "created_at": "2024-12-18T09:20:28+00:00",
                    "traffic_used_bytes": 1462830,
                    "network": "unknown",
                    "upgradable_note": "As our host systems does not support the BTRFS filesystem, this plan upgrades are not yet available.",
                    "project": {
                        "id": 123456,
                        "name": "cherryctl",
                        "bgp": {"enabled": False, "local_asn": 0},
                        "href": "/projects/123456",
                    },
                    "bandwidth_speed_mbps": {"limit": 1000, "maximum": 1000},
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
                    "id": 621229,
                    "name": "Cloud VPS 1",
                    "href": "/servers/621229",
                    "hostname": "test",
                    "password": "123456789",
                    "username": "root",
                    "spot_instance": False,
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
                    "state": "active",
                    "software": {"addons": []},
                    "tags": {},
                    "termination_date": "1970-01-01T00:00:00+00:00",
                    "upgradable": False,
                    "created_at": "2024-12-18T09:20:28+00:00",
                    "traffic_used_bytes": 1462830,
                    "network": "unknown",
                    "upgradable_note": "As our host systems does not support the BTRFS filesystem, this plan upgrades are not yet available.",
                    "project": {
                        "id": 123456,
                        "name": "cherryctl",
                        "bgp": {"enabled": False, "local_asn": 0},
                        "href": "/projects/123456",
                    },
                    "bandwidth_speed_mbps": {"limit": 1000, "maximum": 1000},
                },
                "href": "/ips/1decf524...22ce24df8de",
            },
            {
                "id": "571f30fb...88cf4191",
                "address": "123.123.123.123",
                "address_family": 4,
                "cidr": "123.123.123.123/24",
                "type": "private-ip",
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
                "assigned_to": {
                    "id": 621229,
                    "name": "Cloud VPS 1",
                    "href": "/servers/621229",
                    "hostname": "test",
                    "password": "123456789",
                    "username": "root",
                    "spot_instance": False,
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
                    "state": "active",
                    "software": {"addons": []},
                    "tags": {},
                    "termination_date": "None",
                    "upgradable": False,
                    "created_at": "2024-12-18T09:20:28+00:00",
                    "traffic_used_bytes": 1462830,
                    "network": "unknown",
                    "upgradable_note": "As our host systems does not support the BTRFS filesystem, this plan upgrades are not yet available.",
                    "project": {
                        "id": 123456,
                        "name": "cherryctl",
                        "bgp": {"enabled": False, "local_asn": 0},
                        "href": "/projects/123456",
                    },
                    "bandwidth_speed_mbps": {"limit": 1000, "maximum": 1000},
                },
                "ddos_scrubbing": False,
                "vlan_id": 1234,
                "tags": {},
                "project": {
                    "id": 123456,
                    "name": "cherryctl",
                    "bgp": {"enabled": False, "local_asn": 0},
                    "href": "/projects/123456",
                },
                "targeted_to": {
                    "id": 621229,
                    "name": "Cloud VPS 1",
                    "href": "/servers/621229",
                    "hostname": "test",
                    "password": "123456789",
                    "username": "root",
                    "spot_instance": False,
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
                    "state": "active",
                    "software": {"addons": []},
                    "tags": {},
                    "termination_date": "None",
                    "upgradable": False,
                    "created_at": "2024-12-18T09:20:28+00:00",
                    "traffic_used_bytes": 1462830,
                    "network": "unknown",
                    "upgradable_note": "As our host systems does not support the BTRFS filesystem, this plan upgrades are not yet available.",
                    "project": {
                        "id": 123456,
                        "name": "cherryctl",
                        "bgp": {"enabled": False, "local_asn": 0},
                        "href": "/projects/123456",
                    },
                    "bandwidth_speed_mbps": {"limit": 1000, "maximum": 1000},
                },
                "href": "/ips/571f30fb...88cf4191",
            },
        ],
        "ssh_keys": [],
        "tags": {},
        "termination_date": "None",
        "upgradable": False,
        "created_at": "2024-12-18T09:20:28+00:00",
        "traffic_used_bytes": 1462830,
        "network": "unknown",
        "deployed_image": {"name": "Fedora 41 64bit", "slug": "fedora_41_64bit"},
        "upgradable_note": "As our host systems does not support the BTRFS filesystem, this plan upgrades are not yet available.",
        "project": {
            "id": 123456,
            "name": "cherryctl",
            "bgp": {"enabled": False, "local_asn": 0},
            "href": "/projects/123456",
        },
        "bandwidth_speed_mbps": {"limit": 1000, "maximum": 1000},
    }

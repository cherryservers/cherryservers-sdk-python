"""Cherry Servers Python SDK backup storage unit test fixtures."""

from __future__ import annotations

from typing import Any
from unittest import mock

import pytest

import cherryservers_sdk_python


@pytest.fixture
def backup_storages_client() -> (
    cherryservers_sdk_python.backup_storages.BackupStorageClient
):
    """Initialize backup storage client fixture."""
    return cherryservers_sdk_python.backup_storages.BackupStorageClient(
        api_client=mock.MagicMock()
    )


@pytest.fixture
def backup_storage_resource(
    simple_backup_storage: dict[str, Any],
    backup_storages_client: cherryservers_sdk_python.backup_storages.BackupStorageClient,
) -> cherryservers_sdk_python.backup_storages.BackupStorage:
    """Initialize backup storage resource fixture."""
    return cherryservers_sdk_python.backup_storages.BackupStorage(
        client=backup_storages_client,
        model=cherryservers_sdk_python.backup_storages.BackupStorageModel.model_validate(
            simple_backup_storage
        ),
    )


@pytest.fixture
def simple_backup_storage() -> dict[str, Any]:
    """Initialize simple backup storage fixture."""
    return {
        "id": 622705,
        "status": "deployed",
        "state": "active",
        "public_ip": "123.123.13.123",
        "size_gigabytes": 50,
        "methods": [
            {"name": "ftp", "enabled": True, "processing": False},
            {"name": "smb", "enabled": True, "processing": False},
            {"name": "nfs", "enabled": True, "processing": False},
            {"name": "borg", "enabled": False, "processing": False},
        ],
        "rules": [
            {
                "ip": {
                    "id": "dcc5efa3-5...9347fc",
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
                    "ddos_scrubbing": False,
                    "tags": {},
                    "project": {
                        "id": 123456,
                        "name": "cherryctl",
                        "bgp": {"enabled": False, "local_asn": 0},
                        "href": "/projects/123456",
                    },
                    "href": "/ips/dcc5efa3-5...9347fc",
                },
                "methods": {"borg": True, "ftp": True, "nfs": True, "smb": True},
            },
            {
                "ip": {
                    "id": "d07f2f97-a3...55ee",
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
                    "ddos_scrubbing": False,
                    "vlan_id": 1234,
                    "tags": {},
                    "project": {
                        "id": 123456,
                        "name": "cherryctl",
                        "bgp": {"enabled": False, "local_asn": 0},
                        "href": "/projects/123456",
                    },
                    "href": "/ips/d07f2f97-a3...55ee",
                },
                "methods": {"borg": True, "ftp": True, "nfs": True, "smb": True},
            },
        ],
        "available_addresses": [
            {
                "id": "bab8f...dc87ba",
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
                    "bgp": {
                        "hosts": ["123.123.123.123", "123.123.123.123"],
                        "asn": 12345,
                    },
                    "location": "Lithuania, Šiauliai",
                },
                "routed_to": {
                    "id": "dcc5efa...9347fc",
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
                    "ddos_scrubbing": False,
                    "tags": {},
                    "project": {
                        "id": 123456,
                        "name": "cherryctl",
                        "bgp": {"enabled": False, "local_asn": 0},
                        "href": "/projects/123456",
                    },
                    "href": "/ips/dcc5e...f979347fc",
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
                    "name": "Cloud VPS 1",
                    "href": "/servers/622690",
                    "hostname": "trusted-panda",
                    "region": {
                        "id": 1,
                        "name": "EU-Nord-1",
                        "slug": "eu_nord_1",
                        "region_iso_2": "LT",
                        "href": "/regions/1",
                        "bgp": {
                            "hosts": [
                                "123.123.123.123",
                                "123.123.123.123",
                            ],
                            "asn": 12345,
                        },
                        "location": "Lithuania, Šiauliai",
                    },
                    "state": "active",
                    "project": {
                        "id": 123456,
                        "name": "cherryctl",
                        "bgp": {"enabled": False, "local_asn": 0},
                        "href": "/projects/123456",
                    },
                },
                "href": "/ips/bab8f4a1-...0dfdc87ba",
            },
            {
                "id": "f23f0b...f09b833bb",
                "address": "123.123.123.123",
                "address_family": 4,
                "cidr": "123.123.123.123/24",
                "gateway": "123.123.123.123",
                "type": "primary-ip",
                "region": {
                    "id": 1,
                    "name": "EU-Nord-1",
                    "slug": "eu_nord_1",
                    "region_iso_2": "LT",
                    "href": "/regions/1",
                    "bgp": {
                        "hosts": [
                            "123.123.123.123",
                            "123.123.123.123",
                        ],
                        "asn": 12345,
                    },
                    "location": "Lithuania, Šiauliai",
                },
                "assigned_to": {
                    "id": 622711,
                    "name": "E5-1660v3",
                    "href": "/servers/622711",
                    "hostname": "huge-quail",
                    "region": {
                        "id": 1,
                        "name": "EU-Nord-1",
                        "slug": "eu_nord_1",
                        "region_iso_2": "LT",
                        "href": "/regions/1",
                        "bgp": {
                            "hosts": [
                                "123.123.123.123",
                                "123.123.123.123",
                            ],
                            "asn": 12345,
                        },
                        "location": "Lithuania, Šiauliai",
                    },
                    "state": "active",
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
                    "id": 622711,
                    "name": "E5-1660v3",
                    "href": "/servers/622711",
                    "hostname": "huge-quail",
                    "region": {
                        "id": 1,
                        "name": "EU-Nord-1",
                        "slug": "eu_nord_1",
                        "region_iso_2": "LT",
                        "href": "/regions/1",
                        "bgp": {
                            "hosts": [
                                "123.123.123.123",
                                "123.123.123.123",
                            ],
                            "asn": 12345,
                        },
                        "location": "Lithuania, Šiauliai",
                    },
                    "state": "active",
                    "project": {
                        "id": 123456,
                        "name": "cherryctl",
                        "bgp": {"enabled": False, "local_asn": 0},
                        "href": "/projects/123456",
                    },
                },
                "href": "/ips/f23f0...3bb",
            },
            {
                "id": "5a811e3e-...eb57c66",
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
                        "hosts": [
                            "123.123.123.123",
                            "123.123.123.123",
                        ],
                        "asn": 12345,
                    },
                    "location": "Lithuania, Šiauliai",
                },
                "assigned_to": {
                    "id": 622711,
                    "name": "E5-1660v3",
                    "href": "/servers/622711",
                    "hostname": "huge-quail",
                    "region": {
                        "id": 1,
                        "name": "EU-Nord-1",
                        "slug": "eu_nord_1",
                        "region_iso_2": "LT",
                        "href": "/regions/1",
                        "bgp": {
                            "hosts": [
                                "123.123.123.123",
                                "123.123.123.123",
                            ],
                            "asn": 12345,
                        },
                        "location": "Lithuania, Šiauliai",
                    },
                    "state": "active",
                    "project": {
                        "id": 123456,
                        "name": "cherryctl",
                        "bgp": {"enabled": False, "local_asn": 0},
                        "href": "/projects/123456",
                    },
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
                    "id": 622711,
                    "name": "E5-1660v3",
                    "href": "/servers/622711",
                    "hostname": "huge-quail",
                    "region": {
                        "id": 1,
                        "name": "EU-Nord-1",
                        "slug": "eu_nord_1",
                        "region_iso_2": "LT",
                        "href": "/regions/1",
                        "bgp": {
                            "hosts": [
                                "123.123.123.123",
                                "123.123.123.123",
                            ],
                            "asn": 12345,
                        },
                        "location": "Lithuania, Šiauliai",
                    },
                    "state": "active",
                    "project": {
                        "id": 123456,
                        "name": "cherryctl",
                        "bgp": {"enabled": False, "local_asn": 0},
                        "href": "/projects/123456",
                    },
                },
                "href": "/ips/5a811e3e...1beb57c66",
            },
        ],
        "plan": {
            "id": 743,
            "name": "Backup Storage 50 GB",
            "slug": "backup_50",
            "size_gigabytes": 50,
            "pricing": [
                {
                    "id": 37,
                    "unit": "Hourly",
                    "price": 0.005,
                    "currency": "EUR",
                    "taxed": True,
                }
            ],
            "regions": [
                {
                    "id": 1,
                    "name": "EU-Nord-1",
                    "slug": "eu_nord_1",
                    "region_iso_2": "LT",
                    "href": "/regions/1",
                    "bgp": {
                        "hosts": [
                            "123.123.123.123",
                            "123.123.123.123",
                        ],
                        "asn": 12345,
                    },
                    "location": "Lithuania, Šiauliai",
                }
            ],
            "href": "/plans/743",
        },
        "pricing": {
            "id": 37,
            "currency": "EUR",
            "unit": "Hours",
            "unit_price": 0.004961,
            "discount": 0.0,
            "discount_percentage": False,
            "price_subtotal": 0.0041,
            "taxed": True,
            "price_total": 0.005,
            "price": 0.005,
            "quantity": 1,
            "billable_amount": 0.005,
        },
        "region": {
            "id": 1,
            "name": "EU-Nord-1",
            "slug": "eu_nord_1",
            "region_iso_2": "LT",
            "href": "/regions/1",
            "bgp": {
                "hosts": [
                    "123.123.123.123",
                    "123.123.123.123",
                ],
                "asn": 12345,
            },
            "location": "Lithuania, Šiauliai",
        },
        "href": "/backup-storages/622705",
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


@pytest.fixture
def simple_backup_storage_plan() -> dict[str, Any]:
    """Initialize simple backup storage plan fixture."""
    return {
        "id": 757,
        "name": "Backup Storage 50 GB (Only VDS)",
        "slug": "backup_50",
        "size_gigabytes": 50,
        "pricing": [
            {
                "id": 3,
                "unit": "Monthly",
                "price": 0.0,
                "currency": "EUR",
                "taxed": False,
            },
            {
                "id": 4,
                "unit": "Quarterly",
                "price": 0.0,
                "currency": "EUR",
                "taxed": False,
            },
            {
                "id": 5,
                "unit": "Semiannually",
                "price": 0.0,
                "currency": "EUR",
                "taxed": False,
            },
            {
                "id": 6,
                "unit": "Annually",
                "price": 0.0,
                "currency": "EUR",
                "taxed": False,
            },
            {
                "id": 37,
                "unit": "Hourly",
                "price": 0.0,
                "currency": "EUR",
                "taxed": False,
            },
        ],
        "regions": [
            {
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
            }
        ],
        "href": "/plans/757",
    }

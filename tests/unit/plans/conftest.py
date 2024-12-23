"""Cherry Servers Python SDK plans unit test fixtures."""

from __future__ import annotations

from typing import Any
from unittest import mock

import pytest

import cherryservers_sdk_python.plans


@pytest.fixture
def plans_client() -> cherryservers_sdk_python.plans.PlanClient:
    """Initialize plan client fixture."""
    return cherryservers_sdk_python.plans.PlanClient(api_client=mock.MagicMock())


@pytest.fixture
def plan_resource(
    simple_plan: dict[str, Any],
    plans_client: cherryservers_sdk_python.plans.PlanClient,
) -> cherryservers_sdk_python.plans.Plan:
    """Initialize plan resource fixture."""
    return cherryservers_sdk_python.plans.Plan(
        client=plans_client,
        model=cherryservers_sdk_python.plans.PlanModel.model_validate(simple_plan),
    )


@pytest.fixture
def simple_plan() -> dict[str, Any]:
    """Initialize simple plan fixture."""
    return {
        "id": 86,
        "href": "/plans/e3_1240v3",
        "name": "E3-1240v3",
        "slug": "e3_1240v3",
        "title": "E3-1240v3",
        "type": "baremetal",
        "category": "lightweight",
        "specs": {
            "cpus": {
                "count": 1,
                "name": "E3-1240v3",
                "cores": 4,
                "frequency": 3.4,
                "unit": "GHz",
            },
            "memory": {
                "count": 1,
                "total": 16,
                "unit": "GB",
                "name": "16GB ECC DDRIII ",
            },
            "storage": [
                {
                    "count": 1,
                    "name": "SSD 250GB",
                    "size": 250,
                    "unit": "GB",
                    "type": "SSD",
                }
            ],
            "nics": {"name": "1Gbps"},
            "bandwidth": {"name": "30TB"},
        },
        "pricing": [
            {
                "id": 3,
                "unit": "Monthly",
                "price": 59.29,
                "currency": "EUR",
                "taxed": True,
            },
            {
                "id": 4,
                "unit": "Quarterly",
                "price": 168.9765,
                "currency": "EUR",
                "taxed": True,
            },
            {
                "id": 5,
                "unit": "Semiannually",
                "price": 320.166,
                "currency": "EUR",
                "taxed": True,
            },
            {
                "id": 6,
                "unit": "Annually",
                "price": 604.758,
                "currency": "EUR",
                "taxed": True,
            },
            {
                "id": 37,
                "unit": "Hourly",
                "price": 0.1016,
                "currency": "EUR",
                "taxed": True,
            },
            {
                "id": 38,
                "unit": "Spot hourly",
                "price": 0.0812,
                "currency": "EUR",
                "taxed": True,
            },
        ],
        "available_regions": [
            {
                "id": 1,
                "name": "EU-Nord-1",
                "region_iso_2": "LT",
                "stock_qty": 23,
                "spot_qty": 3,
                "href": "/regions/1",
                "slug": "eu_nord_1",
                "bgp": {"hosts": ["123.123.123.123", "123.123.123.123"], "asn": 12345},
                "location": "Lithuania, Šiauliai",
            }
        ],
    }

"""Cherry Servers Python SDK teams unit test fixtures."""

from __future__ import annotations

from typing import TYPE_CHECKING
from unittest import mock

import pytest

import cherryservers_sdk_python.teams

if TYPE_CHECKING:
    from tests.unit import helpers


@pytest.fixture
def teams_client() -> cherryservers_sdk_python.teams.TeamClient:
    """Initialize team client fixture."""
    return cherryservers_sdk_python.teams.TeamClient(api_client=mock.MagicMock())


@pytest.fixture
def team_resource(
    simple_team: helpers.JSON,
    teams_client: cherryservers_sdk_python.teams.TeamClient,
) -> cherryservers_sdk_python.teams.Team:
    """Initialize team resource fixture."""
    return cherryservers_sdk_python.teams.Team(
        client=teams_client,
        model=cherryservers_sdk_python.teams.TeamModel.model_validate(simple_team),
    )


@pytest.fixture
def simple_team() -> helpers.JSON:
    """Initialize simple team fixture."""
    return {
        "id": 123456,
        "name": " team",
        "credit": {
            "account": {"currency": "EUR"},
            "promo": {"remaining": 669.15, "usage": 6.65, "currency": "EUR"},
            "resources": {
                "pricing": {
                    "price": 0.1228,
                    "taxed": True,
                    "currency": "EUR",
                    "unit": "Hourly",
                },
                "remaining": {"time": 6586, "unit": "Hourly"},
            },
        },
        "billing": {
            "type": "personal",
            "country_iso_2": "LT",
            "vat": {"amount": 21, "valid": False},
            "currency": "EUR",
        },
        "href": "/teams/123456",
    }

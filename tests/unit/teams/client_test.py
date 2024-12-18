"""Unit tests for Cherry Servers Python SDK teams client."""

from __future__ import annotations

from typing import TYPE_CHECKING
from unittest import mock

import pytest

import cherryservers_sdk_python.users
from tests.unit import resource_client_helpers, resource_helpers

if TYPE_CHECKING:
    import requests


class TestClient:
    """Test team client."""

    @pytest.fixture
    def teams_client(self) -> cherryservers_sdk_python.teams.TeamClient:
        """Initialize team client fixture."""
        return cherryservers_sdk_python.teams.TeamClient(api_client=mock.MagicMock())

    def test_get_by_id_success(
        self,
        get_team_successful_response: requests.Response,
        teams_client: cherryservers_sdk_python.teams.TeamClient,
    ) -> None:
        """Test successfully getting a team by ID."""
        resource_client_helpers.check_getter_function(
            get_team_successful_response,
            teams_client,
            lambda: teams_client.get_by_id(123456),
        )

    def test_get_all_success(
        self,
        get_all_teams_successful_response: requests.Response,
        teams_client: cherryservers_sdk_python.teams.TeamClient,
    ) -> None:
        """Test successfully getting all teams."""
        resource_client_helpers.check_listing_function(
            get_all_teams_successful_response,
            teams_client,
            teams_client.get_all,
        )

    def test_create_success(
        self,
        create_team_successful_response: requests.Response,
        teams_client: cherryservers_sdk_python.teams.TeamClient,
    ) -> None:
        """Test successful team creation."""
        creation_resp_json = create_team_successful_response.json()
        resource_client_helpers.check_creation_function(
            create_team_successful_response,
            create_team_successful_response,
            teams_client,
            lambda: teams_client.create(
                cherryservers_sdk_python.teams.CreationRequest(
                    name=creation_resp_json["name"],
                )
            ),
        )

    def test_update_success(
        self,
        update_team_successful_response: requests.Response,
        teams_client: cherryservers_sdk_python.teams.TeamClient,
    ) -> None:
        """Test successfully updating a team.."""
        update_resp_json = update_team_successful_response.json()
        resource_client_helpers.check_update_function(
            update_team_successful_response,
            update_team_successful_response,
            teams_client,
            lambda: teams_client.update(
                update_resp_json["id"],
                cherryservers_sdk_python.teams.UpdateRequest(
                    name=update_resp_json["name"],
                ),
            ),
        )


class TestTeam:
    """Test team resource."""

    @pytest.fixture
    def team(
        self, get_team_successful_response: requests.Response
    ) -> cherryservers_sdk_python.teams.Team:
        """Initialize team fixture."""
        return cherryservers_sdk_python.teams.Team(
            client=cherryservers_sdk_python.teams.TeamClient(
                api_client=mock.MagicMock()
            ),
            model=cherryservers_sdk_python.teams.TeamModel.model_validate(
                get_team_successful_response.json()
            ),
        )

    def test_get_id(
        self,
        team: cherryservers_sdk_python.teams.Team,
        get_team_successful_response: requests.Response,
    ) -> None:
        """Test getting team ID."""
        assert team.get_id() == get_team_successful_response.json()["id"]

    def test_update(
        self,
        team: cherryservers_sdk_python.teams.Team,
        update_team_successful_response: requests.Response,
    ) -> None:
        """Test updating a team."""
        update_resp_json = update_team_successful_response.json()
        resource_helpers.check_update_function(
            update_team_successful_response,
            update_team_successful_response,
            team,
            lambda: team.update(
                cherryservers_sdk_python.teams.UpdateRequest(
                    name=update_resp_json["name"],
                )
            ),
        )

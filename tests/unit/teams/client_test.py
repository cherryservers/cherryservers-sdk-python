"""Unit tests for Cherry Servers Python SDK teams client."""

from __future__ import annotations

from typing import TYPE_CHECKING, cast
from unittest import mock

import pytest

import cherryservers_sdk_python.users

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
        """Test successful team get by ID."""
        cast(
            mock.Mock, teams_client._api_client.get
        ).return_value = get_team_successful_response
        team = teams_client.get_by_id(123456)
        team_expected_model = cherryservers_sdk_python.teams.TeamModel.model_validate(
            get_team_successful_response.json()
        )
        assert team_expected_model == team.get_model()

    def test_get_all_success(
        self,
        get_all_teams_successful_response: requests.Response,
        teams_client: cherryservers_sdk_python.teams.TeamClient,
    ) -> None:
        """Test successful get all teams."""
        cast(
            mock.Mock, teams_client._api_client.get
        ).return_value = get_all_teams_successful_response
        teams = teams_client.get_all()

        assert teams[
            0
        ].get_model() == cherryservers_sdk_python.teams.TeamModel.model_validate(
            get_all_teams_successful_response.json()[0]
        )

        assert teams[
            1
        ].get_model() == cherryservers_sdk_python.teams.TeamModel.model_validate(
            get_all_teams_successful_response.json()[1]
        )

    def test_create_success(
        self,
        create_team_successful_response: requests.Response,
        teams_client: cherryservers_sdk_python.teams.TeamClient,
    ) -> None:
        """Test successful team creation."""
        cast(
            mock.Mock, teams_client._api_client.get
        ).return_value = create_team_successful_response
        cast(
            mock.Mock, teams_client._api_client.post
        ).return_value = create_team_successful_response

        team = teams_client.create(
            creation_schema=cherryservers_sdk_python.teams.CreationRequest(name="test")
        )

        assert (
            team.get_model()
            == cherryservers_sdk_python.teams.TeamModel.model_validate(
                create_team_successful_response.json()
            )
        )

    def test_update_success(
        self,
        update_team_successful_response: requests.Response,
        teams_client: cherryservers_sdk_python.teams.TeamClient,
    ) -> None:
        """Test successful team update."""
        cast(
            mock.Mock, teams_client._api_client.get
        ).return_value = update_team_successful_response
        cast(
            mock.Mock, teams_client._api_client.put
        ).return_value = update_team_successful_response

        team = teams_client.update(
            update_schema=cherryservers_sdk_python.teams.UpdateRequest(
                name="sdk-test-updated"
            ),
            team_id=159248,
        )

        assert (
            team.get_model()
            == cherryservers_sdk_python.teams.TeamModel.model_validate(
                update_team_successful_response.json()
            )
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

    def test_get_model(self, team: cherryservers_sdk_python.teams.Team) -> None:
        """Test getting team model."""
        assert team.get_model() == team._model

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
        cast(
            mock.Mock, team._client._api_client.get
        ).return_value = update_team_successful_response
        cast(
            mock.Mock, team._client._api_client.put
        ).return_value = update_team_successful_response

        update_req = cherryservers_sdk_python.teams.UpdateRequest(
            name="sdk-test-updated"
        )
        team.update(update_req)

        assert team.get_model().name == "sdk-test-updated"

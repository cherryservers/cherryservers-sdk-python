"""Test cherry teams module functionality."""

from __future__ import annotations

import pytest
import requests

import cherry


class TestTeam:
    """Test Team functionality."""

    @pytest.fixture(scope="class")
    def team(self, facade: cherry.facade.CherryApiFacade) -> cherry.teams.Team:
        """Initialize a Cherry Servers Team."""
        creation_req = cherry.teams.CreationRequest(name="cherry-python-sdk-test")
        team = facade.teams.create(creation_req)

        team_model = team.get_model()

        assert team_model.name == creation_req.name

        return team

    def test_get_by_id(
        self, team: cherry.teams.Team, facade: cherry.facade.CherryApiFacade
    ) -> None:
        """Test getting a single team by ID."""
        team_model = team.get_model()
        retrieved_team = facade.teams.get_by_id(team_model.id)
        retrieved_team_model = retrieved_team.get_model()

        assert retrieved_team_model.name == team_model.name

    def test_get_all(
        self, team: cherry.teams.Team, facade: cherry.facade.CherryApiFacade
    ) -> None:
        """Test getting all teams."""
        retrieved_teams = facade.teams.get_all()
        team_model = team.get_model()

        retrieved_team_models = [model.get_model() for model in retrieved_teams]

        assert any(
            team_model.name == retrieved_team_model.name
            for retrieved_team_model in retrieved_team_models
        )

    def test_update(self, team: cherry.teams.Team) -> None:
        """Test updating a team."""
        update_req = cherry.teams.UpdateRequest(name="cherry-python-sdk-test-updated")
        team.update(update_req)

        updated_model = team.get_model()

        assert updated_model.name == update_req.name

    def test_delete(
        self, team: cherry.teams.Team, facade: cherry.facade.CherryApiFacade
    ) -> None:
        """Test deleting a team."""
        team.delete()
        team_model = team.get_model()

        with pytest.raises(requests.exceptions.HTTPError):
            facade.teams.get_by_id(team_model.id)

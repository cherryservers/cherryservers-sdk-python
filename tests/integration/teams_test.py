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

        assert team.model.name == creation_req.name

        return team

    def test_get_by_id(
        self, team: cherry.teams.Team, facade: cherry.facade.CherryApiFacade
    ) -> None:
        """Test getting a single team by ID."""
        retrieved_team = facade.teams.get_by_id(team.model.id)

        assert retrieved_team.model.name == team.model.name

    def test_get_all(
        self, team: cherry.teams.Team, facade: cherry.facade.CherryApiFacade
    ) -> None:
        """Test getting all teams."""
        teams = facade.teams.get_all()

        assert any(
            team.model.name == retrieved_team.model.name for retrieved_team in teams
        )

    def test_update(self, team: cherry.teams.Team) -> None:
        """Test updating a team."""
        update_req = cherry.teams.UpdateRequest(name="cherry-python-sdk-test-updated")
        team.update(update_req)

        assert team.model.name == update_req.name

    def test_delete(
        self, team: cherry.teams.Team, facade: cherry.facade.CherryApiFacade
    ) -> None:
        """Test deleting a team."""
        team.delete()

        with pytest.raises(requests.exceptions.HTTPError):
            facade.teams.get_by_id(team.model.id)

"""Test cherryservers_sdk_python plans module functionality."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import cherryservers_sdk_python


class TestPlan:
    """Test Plan functionality."""

    def test_get_by_team(
        self, facade: cherryservers_sdk_python.facade.CherryApiFacade, team_id: int
    ) -> None:
        """Test getting all plans available for a team."""
        facade.plans.list_by_team(team_id)

    def test_get_by_id_or_slug(
        self, facade: cherryservers_sdk_python.facade.CherryApiFacade
    ) -> None:
        """Test getting a plan by ID or slug."""
        plan = facade.plans.get_by_id_or_slug("B1-1-1gb-20s-shared")

        assert plan.get_model().slug == "B1-1-1gb-20s-shared"

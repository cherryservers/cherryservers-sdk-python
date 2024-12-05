"""Test cherry plans module functionality."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import cherry


class TestPlan:
    """Test Plan functionality."""

    def test_get_by_team(
        self, facade: cherry.facade.CherryApiFacade, team_id: int
    ) -> None:
        """Test getting all plans available for a team."""
        facade.plans.list_by_team(team_id)

    def test_get_by_id_or_slug(self, facade: cherry.facade.CherryApiFacade) -> None:
        """Test getting a plan by ID or slug."""
        plan = facade.plans.get_by_id_or_slug("cloud_vps_1")

        assert plan.get_model().slug == "cloud_vps_1"

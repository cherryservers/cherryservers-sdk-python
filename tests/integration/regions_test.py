"""Test cherry regions module functionality."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import cherry


class TestRegion:
    """Test Region functionality."""

    def test_get_all(self, facade: cherry.facade.CherryApiFacade) -> None:
        """Test getting all regions."""
        retrieved_regions = facade.regions.get_all()
        retrieved_region_models = [
            region_model.get_model_copy() for region_model in retrieved_regions
        ]

        assert any(
            region_model.id == 1 and region_model.slug == "eu_nord_1"
            for region_model in retrieved_region_models
        )

    def test_get_by_id(self, facade: cherry.facade.CherryApiFacade) -> None:
        """Test getting a region by id."""
        region = facade.regions.get_by_id(1)

        assert region.get_model_copy().slug == "eu_nord_1"

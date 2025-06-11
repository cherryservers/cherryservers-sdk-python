"""Test cherryservers_sdk_python regions module functionality."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import cherryservers_sdk_python


class TestRegion:
    """Test Region functionality."""

    def test_get_all(
        self, facade: cherryservers_sdk_python.facade.CherryApiFacade
    ) -> None:
        """Test getting all regions."""
        retrieved_regions = facade.regions.get_all()
        retrieved_region_models = [
            region_model.get_model() for region_model in retrieved_regions
        ]

        assert any(
            region_model.id == 1 and region_model.slug == "LT-Siauliai"
            for region_model in retrieved_region_models
        )

    def test_get_by_id(
        self, facade: cherryservers_sdk_python.facade.CherryApiFacade
    ) -> None:
        """Test getting a region by id."""
        region = facade.regions.get_by_id(1)

        assert region.get_model().slug == "LT-Siauliai"

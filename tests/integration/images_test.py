"""Test cherry images module functionality."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import cherry


class TestImage:
    """Test User functionality."""

    def test_get_by_plan(self, facade: cherry.facade.CherryApiFacade) -> None:
        """Test getting a list of images by plan slug."""
        images = facade.images.get_by_plan("cloud_vps_1")

        retrieved_image_models = [image.get_model() for image in images]

        assert any(
            image_model.slug == "debian_12_64bit"
            for image_model in retrieved_image_models
        )

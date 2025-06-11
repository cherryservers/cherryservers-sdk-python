"""Test cherryservers_sdk_python images module functionality."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import cherryservers_sdk_python


class TestImage:
    """Test User functionality."""

    def test_get_by_plan(
        self, facade: cherryservers_sdk_python.facade.CherryApiFacade
    ) -> None:
        """Test getting a list of images by plan slug."""
        images = facade.images.list_by_plan("B1-1-1gb-20s-shared")

        retrieved_image_models = [image.get_model() for image in images]

        assert any(
            image_model.slug == "debian_12_64bit"
            for image_model in retrieved_image_models
        )

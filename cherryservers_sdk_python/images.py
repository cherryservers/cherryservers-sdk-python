"""Cherry Servers image resource management module."""

from __future__ import annotations

from pydantic import Field

from cherryservers_sdk_python import _base, plans


class ImageModel(_base.ResourceModel):
    """Cherry Servers image model.

    This model is frozen by default,
    since it represents an actual Cherry Servers image resource state.

    Attributes:
        id(int): ID of the image.
        name(str | None): Full name of the image.
        slug(str | None): Slug of the image name.
        pricing(list[cherryservers_sdk_python.plans.PricingModel] | None):
         Image pricing data.

    """

    id: int = Field(description="ID of the image.")
    name: str | None = Field(description="Full name of the image.", default=None)
    slug: str | None = Field(description="Slug of the image name.", default=None)
    pricing: list[plans.PricingModel] | None = Field(
        description="Image pricing data.", default=None
    )


class ImageClient(_base.ResourceClient):
    """Cherry Servers image client.

    Manage Cherry Servers image resources. This class should typically be initialized by
    :class:`cherryservers_sdk_python.facade.CherryApiFacade`.

    Example:
        .. code-block:: python

            facade = cherryservers_sdk_python.facade.CherryApiFacade(token="my-token")

            # Retrieve a list of available OSes for a server plan.
            images = facade.images.get_by_plan("B1-1-1gb-20s-shared")

    """

    def list_by_plan(self, plan_slug: str) -> list[Image]:
        """Retrieve a list of available OSes for a server plan."""
        response = self._api_client.get(
            f"plans/{plan_slug}/images", None, self.request_timeout
        )
        images: list[Image] = []
        for value in response.json():
            image_model = ImageModel.model_validate(value)
            images.append(Image(self, image_model))

        return images


class Image(_base.Resource[ImageClient, ImageModel]):
    """Cherry Servers image resource.

    This class represents an existing Cherry Servers resource
    and should only be initialized by :class:`ImageClient`.
    """

    def get_id(self) -> int:
        """Get resource ID."""
        return self._model.id

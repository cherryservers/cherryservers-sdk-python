"""Cherry Servers region resource management module."""

from __future__ import annotations

from pydantic import Field

from cherry import _base


class RegionBGPModel(_base.ResourceModel):
    """Cherry Servers region BPG model.

    This model is frozen by default,
    since it represents an actual Cherry Servers region BGP resource state.

    Attributes:
        hosts (list[str] | None): Host IP addresses.
        asn (int | None): Region ASN.

    """

    hosts: list[str] | None = Field(description="Host IP addresses.", default=None)
    asn: int | None = Field(description="Region ASN.", default=None)


class RegionModel(_base.ResourceModel):
    """Cherry Servers region model.

    This model is frozen by default,
    since it represents an actual Cherry Servers region resource state.

    Attributes:
        id (int): ID of the region.
        name (str | None): Name of the region.
        slug (str | None): Slug of the regions name.
        region_iso_2 (str | None): Region ISO 2 country code.
        bgp (cherry.regions.RegionBGPModel | None): Region BGP.
        location (str | None): Region server location.
        href (str | None): Region href.

    """

    id: int = Field(description="ID of the region.")
    name: str | None = Field(description="Name of the region.", default=None)
    slug: str | None = Field(description="Slug of the regions name.", default=None)
    region_iso_2: str | None = Field(
        description="Region ISO 2 country code.", default=None
    )
    bgp: RegionBGPModel | None = Field(description="Region BPG.", default=None)
    location: str | None = Field(description="Region server location.", default=None)
    href: str | None = Field(description="Region href.", default=None)


class RegionClient(_base.ResourceClient):
    """Cherry Servers region client.

    Manage Cherry Servers region resources.
    This class should typically be initialized by
    :class:`cherry.facade.CherryApiFacade`.

    Example:
        .. code-block:: python

            facade = cherry.facade.CherryApiFacade(token="my-token")

            # Retrieve by ID.
            region = facade.regions.get_by_id(1)

            # Retrieve all regions.
            regions = facade.regions.get_all()

    """

    def get_by_id(self, region_id: int) -> Region:
        """Retrieve a region by ID."""
        response = self._api_client.get(f"regions/{region_id}", None, 5)
        region_model = RegionModel.model_validate(response.json())
        return Region(self, region_model)

    def get_all(self) -> list[Region]:
        """Retrieve all regions."""
        response = self._api_client.get("regions", None, 5)
        regions: list[Region] = []
        for value in response.json():
            region_model = RegionModel.model_validate(value)
            regions.append(Region(self, region_model))

        return regions


class Region(_base.Resource[RegionClient, RegionModel]):
    """Cherry Servers region resource.

    This class represents an existing Cherry Servers resource
    and should only be initialized by :class:`RegionClient`.
    """

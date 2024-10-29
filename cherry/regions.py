"""Cherry Servers region resource management module."""

from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import Field

from cherry import _models

if TYPE_CHECKING:
    from cherry import _client


class RegionBGPModel(_models.DefaultModel):
    """Cherry Servers region BPG model.

    This model is frozen by default,
    since it represents an actual Cherry Servers region BGP resource state.

    Attributes:
        hosts (list[str]): Host IP addresses.
        asn (int): Region ASN.

    """

    hosts: list[str] = Field(description="Host IP addresses.")
    asn: int = Field(description="Region ASN.")


class RegionModel(_models.DefaultModel):
    """Cherry Servers region model.

    This model is frozen by default,
    since it represents an actual Cherry Servers region resource state.

    Attributes:
        id (int): ID of the region.
        name (str): Name of the region.
        slug (str): Slug of the regions name.
        region_iso_2 (str): Region ISO 2 country code.
        bgp (cherry.regions.RegionBGPModel): Region BGP.
        location (str): Region server location.
        href (str): Region href.

    """

    id: int = Field(description="ID of the region.")
    name: str = Field(description="Name of the region.")
    slug: str = Field(description="Slug of the regions name.")
    region_iso_2: str = Field(description="Region ISO 2 country code.")
    bgp: RegionBGPModel = Field(description="Region BPG.")
    location: str = Field(description="Region server location.")
    href: str = Field(description="Region href.")


class Region:
    """Cherry Servers region resource.

    This class represents an existing Cherry Servers resource
    and should only be initialized by :class:`RegionClient`.

    Attributes:
        model (RegionModel): Cherry Servers region model.
            This is a Pydantic model that contains region data.
            A standard dictionary can be extracted with ``model.model_dump()``.

    """

    def __init__(self, client: RegionClient, model: RegionModel) -> None:
        """Initialize a Cherry Servers region resource."""
        self._client = client
        self.model = model


class RegionClient:
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

    def __init__(self, api_client: _client.CherryApiClient) -> None:
        """Initialize a Cherry Servers region client."""
        self._api_client = api_client

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

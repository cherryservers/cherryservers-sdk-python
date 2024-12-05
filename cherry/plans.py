"""Cherry Servers plan resource management module."""

from __future__ import annotations

from pydantic import Field

from cherry import _base, regions


class AvailableRegionsModel(regions.RegionModel):
    """Cherry Servers plan available regions model.

    This model is frozen by default,
    since it represents an actual Cherry Servers plan available region resource state.

    Inherits all attributes of :class:`cherry.regions.RegionModel`.

    Attributes:
        stock_qty (int | None): The number servers in stock.
        spot_qty (int | None): The number of servers as spot instances in stock.

    """

    stock_qty: int | None = Field(
        description="The number servers in stock.", default=None
    )
    spot_qty: int | None = Field(
        description="The number of servers as spot instances in stock.", default=None
    )


class BandwidthModel(_base.ResourceModel):
    """Cherry Servers plan specs bandwidth model.

    This model is frozen by default,
    since it represents an actual Cherry Servers plan specs bandwidth resource state.

    Attributes:
        name (str | None): Bandwidth name.

    """

    name: str | None = Field(description="Bandwidth name.", default=None)


class NicsModel(_base.ResourceModel):
    """Cherry Servers plan specs network interface controllers model.

    This model is frozen by default,
    since it represents an actual Cherry Servers plan specs
    network interface controllers state.

    Attributes:
        name (str | None): NICS name.

    """

    name: str | None = Field(description="NICS name.", default=None)


class RaidModel(_base.ResourceModel):
    """Cherry Servers plan specs RAID model.

    This model is frozen by default,
    since it represents an actual Cherry Servers plan specs
    RAID resource state.

    Attributes:
        name (str | None): RAID name.

    """

    name: str | None = Field(description="RAID name.", default=None)


class StorageModel(_base.ResourceModel):
    """Cherry Servers plan specs storage model.

    This model is frozen by default,
    since it represents an actual Cherry Servers plan specs
    storage resource state.

    Attributes:
        name (str | None): Storage device name.
        count (int | None): The number of storage devices.
        size (float | None): The size of the storage devices.
        unit (str | None): Storage device size measurement unit.

    """

    name: str | None = Field(description="Storage device name.", default=None)
    count: int | None = Field(
        description="The number of storage devices.", default=None
    )
    size: float | None = Field(
        description="The size of the storage devices.", default=None
    )
    unit: str | None = Field(
        description="Storage device size measurement unit.", default=None
    )


class MemoryModel(_base.ResourceModel):
    """Cherry Servers plan specs memory model.

    This model is frozen by default,
    since it represents an actual Cherry Servers plan specs
    memory resource state.

    Attributes:
        name (str | None): Memory device name.
        count (int | None): The number of memory devices.
        total (int | None): The total capacity of the memory devices.
        unit (str | None): Memory device size measurement unit.

    """

    name: str | None = Field(description="Storage device name.", default=None)
    count: int | None = Field(description="The number of memory devices.", default=None)
    total: int | None = Field(
        description="The total capacity of the memory devices.", default=None
    )
    unit: str | None = Field(
        description="Memory device size measurement unit.", default=None
    )


class CPUModel(_base.ResourceModel):
    """Cherry Servers plan specs CPU model.

    This model is frozen by default,
    since it represents an actual Cherry Servers plan specs
    CPU resource state.

    Attributes:
        name (str | None): CPU device name.
        count (int | None): The number of CPU devices.
        cores (int | None): The number of CPU cores.
        frequency (float | None): The frequency of the CPU cores.
        unit (str | None): CPU core frequency measurement unit.

    """

    name: str | None = Field(description="CPU device name.", default=None)
    count: int | None = Field(description="The number of CPU devices.", default=None)
    cores: int | None = Field(description="The number of CPU cores.", default=None)
    frequency: float | None = Field(
        description="The frequency of the CPU cores.", default=None
    )
    unit: str | None = Field(
        description="CPU core frequency measurement unit.", default=None
    )


class SpecsModel(_base.ResourceModel):
    """Cherry Servers plan specs model.

    This model is frozen by default,
    since it represents an actual Cherry Servers plan specs resource state.

    Attributes:
        cpus (cherry.plans.CPUModel | None): CPU device data.
        memory (cherry.plans.MemoryModel | None): Memory device data.
        storage (list[cherry.plans.StorageModel] | None): Storage device data.
        raid (cherry.plans.RaidModel | None): RAID data.
        nics (cherry.plans.NicsModel | None): NICS device data.
        bandwidth (cherry.plans.BandwidthModel | None): Bandwidth data.

    """

    cpus: CPUModel | None = Field(description="CPU device data.", default=None)
    memory: MemoryModel | None = Field(description="Memory device data.", default=None)
    storage: list[StorageModel] | None = Field(
        description="Storage device data.", default=None
    )
    raid: RaidModel | None = Field(description="RAID data.", default=None)
    nics: NicsModel | None = Field(description="NICS device data.", default=None)
    bandwidth: BandwidthModel | None = Field(
        description="Bandwidth data.", default=None
    )


class PricingModel(_base.ResourceModel):
    """Cherry Servers pricing model.

    This model is frozen by default,
    since it represents an actual Cherry Servers pricing resource state.

    Attributes:
        price (float | None): Price.
        taxed (bool | None): Whether tax is applied.
        currency (str | None): Currency type.
        unit (str | None): Time unit type.

    """

    price: float | None = Field(description="Price.", default=None)
    taxed: bool | None = Field(description="Whether tax is applied.", default=None)
    currency: str | None = Field(description=" Currency type.", default=None)
    unit: str | None = Field(description="Time unit type.", default=None)


class PlanModel(_base.ResourceModel):
    """Cherry Servers plan model.

    This model is frozen by default,
    since it represents an actual Cherry Servers plan resource state.

    Attributes:
        id (int): Plan ID.
        name (str | None): Plan full name.
        slug (str | None): Plan name slug.
        type (str | None): Plan type, such as `baremetal` or `premium-vds`.
        specs (cherry.plans.SpecsModel | None): Plan specs.
        pricing (list[cherry.plans.PricingModel] | None): Plan pricing.
        available_regions (list[cherry.plans.AvailableRegionsModel] | None):
         Available regions for the plan.

    """

    id: int = Field(description="Plan ID.")
    name: str | None = Field(description="Plan full name.", default=None)
    slug: str | None = Field(description="Plan name slug.", default=None)
    type: str | None = Field(
        description="Plan type, such as `baremetal` or `premium-vds`.", default=None
    )
    specs: SpecsModel | None = Field(description="Plan specs.", default=None)
    pricing: list[PricingModel] | None = Field(
        description="Plan pricing.", default=None
    )
    available_regions: list[AvailableRegionsModel] | None = Field(
        description="Available regions for the plan.", default=None
    )


class PlanClient(_base.ResourceClient):
    """Cherry Servers server plan client.

    Manage Cherry Servers plan resources.
    This class should typically be initialized by
    :class:`cherry.facade.CherryApiFacade`.

    Example:
        .. code-block:: python

            facade = cherry.facade.CherryApiFacade(token)

            # Get a list of all team permitted plans.
            plans = facade.plans.get_by_team(123456):

            # Get a plan by id (or slug).
            plan = facade.plans.get_by_id_or_slug("premium_vds_2")

    """

    def get_by_id_or_slug(self, plan_id_or_slug: int | str) -> Plan:
        """Retrieve a plan by ID or slug."""
        response = self._api_client.get(
            f"plans/{plan_id_or_slug}",
            {"fields": "plan,specs,pricing,region,href"},
            10,
        )
        plan_model = PlanModel.model_validate(response.json())
        return Plan(self, plan_model)

    def list_by_team(self, team_id: int) -> list[Plan]:
        """Get all plans that are available to a team."""
        response = self._api_client.get(
            f"teams/{team_id}/plans",
            {"fields": "plan,specs,pricing,region,href"},
            10,
        )
        plans: list[Plan] = []
        for value in response.json():
            plan_model = PlanModel.model_validate(value)
            plans.append(Plan(self, plan_model))

        return plans


class Plan(_base.Resource[PlanClient, PlanModel]):
    """Cherry Servers server plan resource.

    This class represents an existing Cherry Servers resource
    and should only be initialized by :class:`PlanClient`.
    """

    def get_id(self) -> int:
        """Get resource ID."""
        return self._model.id

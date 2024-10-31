"""Cherry Servers plan resource management module."""

from __future__ import annotations

from pydantic import Field

from cherry import _client, _models, regions


class AvailableRegionsModel(regions.RegionModel):
    """Cherry Servers plan available regions model.

    This model is frozen by default,
    since it represents an actual Cherry Servers plan available region resource state.

    Inherits all attributes of :class:`cherry.regions.RegionModel`.

    Attributes:
        stock_qty (int): The number servers in stock.
        spot_qty (int): The number of servers as spot instances in stock.

    """

    stock_qty: int = Field(description="The number servers in stock.")
    spot_qty: int = Field(
        description="The number of servers as spot instances in stock."
    )


class BandwidthModel(_models.DefaultModel):
    """Cherry Servers plan specs bandwidth model.

    This model is frozen by default,
    since it represents an actual Cherry Servers plan specs bandwidth resource state.

    Attributes:
        name (str): Bandwidth name.

    """

    name: str = Field(description="Bandwidth name.")


class NicsModel(_models.DefaultModel):
    """Cherry Servers plan specs network interface controllers model.

    This model is frozen by default,
    since it represents an actual Cherry Servers plan specs
    network interface controllers state.

    Attributes:
        name (str): NICS name.

    """

    name: str = Field(description="NICS name.")


class RaidModel(_models.DefaultModel):
    """Cherry Servers plan specs RAID model.

    This model is frozen by default,
    since it represents an actual Cherry Servers plan specs
    RAID resource state.

    Attributes:
        name (str): RAID name.

    """

    name: str = Field(description="RAID name.")


class StorageModel(_models.DefaultModel):
    """Cherry Servers plan specs storage model.

    This model is frozen by default,
    since it represents an actual Cherry Servers plan specs
    storage resource state.

    Attributes:
        name (str): Storage device name.
        count (int): The number of storage devices.
        size (float): The size of the storage devices.
        unit (str): Storage device size measurement unit.

    """

    name: str = Field(description="Storage device name.")
    count: int = Field(description="The number of storage devices.")
    size: float = Field(description="The size of the storage devices.")
    unit: str = Field(description="Storage device size measurement unit.")


class MemoryModel(_models.DefaultModel):
    """Cherry Servers plan specs memory model.

    This model is frozen by default,
    since it represents an actual Cherry Servers plan specs
    memory resource state.

    Attributes:
        name (str): Memory device name.
        count (int): The number of memory devices.
        total (int): The total capacity of the memory devices.
        unit (str): Memory device size measurement unit.

    """

    name: str = Field(description="Storage device name.")
    count: int = Field(description="The number of memory devices.")
    total: int = Field(description="The total capacity of the memory devices.")
    unit: str = Field(description="Memory device size measurement unit.")


class CPUModel(_models.DefaultModel):
    """Cherry Servers plan specs CPU model.

    This model is frozen by default,
    since it represents an actual Cherry Servers plan specs
    CPU resource state.

    Attributes:
        name (str): CPU device name.
        count (int): The number of CPU devices.
        cores (int): The number of CPU cores.
        frequency (float): The frequency of the CPU cores.
        unit (str): CPU core frequency measurement unit.

    """

    name: str = Field(description="CPU device name.")
    count: int = Field(description="The number of CPU devices.")
    cores: int = Field(description="The number of CPU cores.")
    frequency: float = Field(description="The frequency of the CPU cores.")
    unit: str = Field(description="CPU core frequency measurement unit.")


class SpecsModel(_models.DefaultModel):
    """Cherry Servers plan specs model.

    This model is frozen by default,
    since it represents an actual Cherry Servers plan specs resource state.

    Attributes:
        cpus (cherry.plans.CPUModel): CPU device data.
        memory (cherry.plans.MemoryModel): Memory device data.
        storage (list[cherry.plans.StorageModel]): Storage device data.
        raid (cherry.plans.RaidModel | None): RAID data.
        nics (cherry.plans.NicsModel): NICS device data.
        bandwidth (cherry.plans.BandwidthModel | None): Bandwidth data.

    """

    cpus: CPUModel = Field(description="CPU device data.")
    memory: MemoryModel = Field(description="Memory device data.")
    storage: list[StorageModel] = Field(description="Storage device data.")
    raid: RaidModel | None = Field(description="RAID data.", default=None)
    nics: NicsModel = Field(description="NICS device data.")
    bandwidth: BandwidthModel | None = Field(
        description="Bandwidth data.", default=None
    )


class PricingModel(_models.DefaultModel):
    """Cherry Servers pricing model.

    This model is frozen by default,
    since it represents an actual Cherry Servers pricing resource state.

    Attributes:
        price (float): Price.
        taxed (bool): Whether tax is applied.
        currency (str): Currency type.
        unit (str): Time unit type.

    """

    price: float = Field(description="Price.")
    taxed: bool = Field(description="Whether tax is applied.")
    currency: str = Field(description=" Currency type.")
    unit: str = Field(description="Time unit type.")


class PlanModel(_models.DefaultModel):
    """Cherry Servers plan model.

    This model is frozen by default,
    since it represents an actual Cherry Servers plan resource state.

    Attributes:
        id (int): Plan ID.
        name (str): Plan full name.
        slug (str): Plan name slug.
        type (str): Plan type, such as `baremetal` or `premium-vds`.
        specs (cherry.plans.SpecsModel): Plan specs.
        pricing (list[cherry.plans.PricingModel]): Plan pricing.
        available_regions (list[cherry.plans.AvailableRegionsModel] | None):
        Available regions for the plan.

    """

    id: int = Field(description="Plan ID.")
    name: str = Field(description="Plan full name.")
    slug: str = Field(description="Plan name slug.")
    type: str = Field(description="Plan type, such as `baremetal` or `premium-vds`.")
    specs: SpecsModel = Field(description="Plan specs.")
    pricing: list[PricingModel] = Field(description="Plan pricing.")
    available_regions: list[AvailableRegionsModel] | None = Field(
        description="Available regions for the plan.", default=None
    )


class Plan:
    """Cherry Servers server plan resource.

    This class represents an existing Cherry Servers resource
    and should only be initialized by :class:`PlanClient`.

    Attributes:
        model (PlanModel): Cherry Servers server plan model.
            This is a Pydantic model that contains plan data.
            A standard dictionary can be extracted with ``model.model_dump()``.

    """

    def __init__(self, client: PlanClient, model: PlanModel) -> None:
        """Initialize a Cherry Servers plan resource."""
        self._client = client
        self.model = model


class PlanClient:
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

    def __init__(self, api_client: _client.CherryApiClient) -> None:
        """Initialize a Cherry Servers plan client."""
        self._api_client = api_client

    def get_by_id_or_slug(self, plan_id_or_slug: int | str) -> Plan:
        """Retrieve a plan by ID or slug."""
        response = self._api_client.get(
            f"plans/{plan_id_or_slug}",
            {"fields": "plan,specs,pricing,region,href"},
            10,
        )
        plan_model = PlanModel.model_validate(response.json())
        return Plan(self, plan_model)

    def get_by_team(self, team_id: int) -> list[Plan]:
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

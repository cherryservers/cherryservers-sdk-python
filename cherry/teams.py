"""Cherry Servers teams resource management module."""

from __future__ import annotations

from pydantic import Field

from cherry import _client, _models, request_schemas
from cherry.pricing import PricingModel


class RemainingTimeModel(_models.DefaultModel):
    """Cherry Servers team credit resource remaining time model.

    This model is frozen by default,
    since it represents an actual Cherry Servers credit resource remaining time state.
    Here, resources refers to infrastructure objects that have a real cost.

    Attributes:
        time (int): Remaining time at the current usage rate and credit.
        unit (str): Time unit type.

    """

    time: int = Field(
        description="Remaining time at the current usage rate and credit."
    )
    unit: str = Field(description="Time unit type.")


class ResourcesModel(_models.DefaultModel):
    """Cherry Servers team credit resource detail model.

    This model is frozen by default,
    since it represents an actual Cherry Servers teams credit resources state.
    Here, resources refers to infrastructure objects that have a real cost.

    Attributes:
        pricing (cherry.pricing.PricingModel): Team resource pricing data.
        remaining (cherry.teams.RemainingTimeModel): Team resource remaining time data.

    """

    pricing: PricingModel = Field(description="Team resource pricing data.")
    remaining: RemainingTimeModel = Field(
        description="Team resource remaining time data."
    )


class CreditDetailsModel(_models.DefaultModel):
    """Cherry Servers team credit details model.

    This model is frozen by default,
    since it represents an actual Cherry Servers team credit detail resource state.

    Attributes:
        remaining (float): Remaining credit.
        usage (float): Credit usage rate.
        currency (str): Credit currency.

    """

    remaining: float = Field(description="Remaining credit.")
    usage: float = Field(description="Credit usage rate.")
    currency: str = Field(description="Credit currency.")


class CreditModel(_models.DefaultModel):
    """Cherry Servers team credit model.

    This model is frozen by default,
    since in represents an actual Cherry Servers team credit resource state.

    Attributes:
        account (cherry.teams.CreditDetailsModel): Account credit details.
        promo (cherry.teams.CreditDetailsModel): Promotional credit details.
        resources (cherry.teams.ResourcesModel): Resources credit details.

    """

    account: CreditDetailsModel = Field(description="Account credit details.")
    promo: CreditDetailsModel = Field(description="Promotional credit details.")
    resources: ResourcesModel = Field(description="Resources credit details.")


class VatModel(_models.DefaultModel):
    """Cherry Servers team VAT model.

    This model is frozen by default,
    since it represents an actual Cherry Servers team VAT resource state.

    Attributes:
        amount (int): VAT rate.
        number (str): Amount of paid VAT.
        valid (bool): Whether VAT has been applied.

    """

    amount: int = Field(description="VAT rate.")
    number: str = Field(description="Amount of paid VAT.")
    valid: bool = Field(description="Whether VAT has been applied.")


class BillingModel(_models.DefaultModel):
    """Cherry Servers team billing model.

    This model is frozen by default,
    since it represents an actual Cherry Servers team billing resource state.

    Attributes:
        type (str): Billing type: `personal` or `business`.
        company_name (str | None): Company name, if applicable.
        company_code (str | None): Company code, if applicable.
        first_name (str | None): First name, if applicable.
        last_name (str | None): Last name, if applicable.
        address_1 (str | None): First address line, if applicable.
        address_2 (str | None): Last address line, if applicable.
        country_iso_2 (str | None): Country code, if applicable.
        city (str | None): City, if applicable.
        vat (cherry.teams.VatModel): VAT data.
        currency (str): Currency type.

    """

    type: str = Field(description="Billing type: `personal` or `business`.")
    company_name: str | None = Field(
        description="Company name, if applicable.", default=None
    )
    company_code: str | None = Field(
        description="Company code, if applicable.", default=None
    )
    first_name: str | None = Field(
        description="First name, if applicable.", default=None
    )
    last_name: str | None = Field(description="Last name, if applicable.", default=None)
    address_1: str | None = Field(
        description="First address line, if applicable.", default=None
    )
    address_2: str | None = Field(
        description="Last address line, if applicable.", default=None
    )
    country_iso_2: str | None = Field(
        description="Country code, if applicable.", default=None
    )
    city: str | None = Field(description="City, if applicable.", default=None)
    vat: VatModel = Field(description="VAT data.")
    currency: str = Field(description="Currency type.")


class TeamModel(_models.DefaultModel):
    """Cherry Servers team model.

    This model is frozen by default,
    since it represents an actual Cherry Servers team resource state.

    Attributes:
        id (int): Team ID.
        name (str): Team name.
        credit (cherry.teams.CreditModel): Team credit data.
        billing (cherry.teams.BillingModel): Team billing data.
        href (str): Team href.

    """

    id: int = Field(description="Team ID.")
    name: str = Field(description="Team name.")
    credit: CreditModel = Field(description="Team credit data.")
    billing: BillingModel = Field(description="Team billing data.")
    href: str = Field(description="Team href.")


class Team:
    """Cherry Servers team resource.

    This class represents an existing Cherry Servers resource
    and should only be initialized by :class:`TeamClient`.

    Attributes:
        model (TeamModel): Cherry Servers team model.
            This is a Pydantic model that contains team data.
            A standard dictionary can be extracted with ``model.model_dump()``.

    """

    def __init__(self, client: TeamClient, model: TeamModel) -> None:
        """Initialize a Cherry Servers team resource."""
        self._client = client
        self.model = model

    def delete(self) -> None:
        """Delete Cherry Servers team resource."""
        self._client.delete(self.model.id)

    def update(self, update_schema: request_schemas.teams.UpdateRequest) -> None:
        """Update Cherry Servers team resource."""
        updated = self._client.update(self.model.id, update_schema)
        self.model = updated.model


class TeamClient:
    """Cherry Servers team client.

    Manage Cherry Servers team resources.
    This class should typically be initialized by
    :class:`cherry.facade.CherryApiFacade`.

    Example:
        .. code-block:: python

            # Get all teams.
            teams = facade.teams.get_all()

            # Get a team by ID.
            team = facade.teams.get_by_id(123456)

            # Create a team.
            create_req = cherry.request_schemas.teams.CreationRequest(
                name="python-sdk-test", currency="EUR"
            )
            new_team = facade.teams.create(create_req)

            # Update team.
            update_req = cherry.request_schemas.teams.UpdateRequest(
                name="python-sdk-test-updated"
            )
            new_team.update(update_req)

            # Delete team.
            new_team.delete()

    """

    def __init__(self, api_client: _client.CherryApiClient) -> None:
        """Initialize a Cherry Servers team client."""
        self._api_client = api_client

    def get_by_id(self, team_id: int) -> Team:
        """Retrieve a team by ID."""
        response = self._api_client.get(
            f"teams/{team_id}",
            None,
            5,
        )
        team_model = TeamModel.model_validate(response.json())
        return Team(self, team_model)

    def get_all(self) -> list[Team]:
        """Get all teams."""
        response = self._api_client.get("teams", None, 5)
        teams: list[Team] = []
        for value in response.json():
            team_model = TeamModel.model_validate(value)
            teams.append(Team(self, team_model))

        return teams

    def create(self, creation_schema: request_schemas.teams.CreationRequest) -> Team:
        """Create a new team."""
        response = self._api_client.post("teams", creation_schema, None, 15)
        return self.get_by_id(response.json()["id"])

    def delete(self, team_id: int) -> None:
        """Delete a team by ID."""
        self._api_client.delete(f"teams/{team_id}", None, 5)

    def update(
        self, team_id: int, update_schema: request_schemas.teams.UpdateRequest
    ) -> Team:
        """Update a team by ID."""
        response = self._api_client.put(f"teams/{team_id}", update_schema, None, 10)
        return self.get_by_id(response.json()["id"])

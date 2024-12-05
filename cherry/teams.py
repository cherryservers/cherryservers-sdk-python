"""Cherry Servers teams resource management module."""

from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import Field

from cherry import _base

if TYPE_CHECKING:
    from cherry.plans import PricingModel


class RemainingTimeModel(_base.ResourceModel):
    """Cherry Servers team credit resource remaining time model.

    This model is frozen by default,
    since it represents an actual Cherry Servers credit resource remaining time state.
    Here, resources refers to infrastructure objects that have a real cost.

    Attributes:
        time (int | None): Remaining time at the current usage rate and credit.
        unit (str | None): Time unit type.

    """

    time: int | None = Field(
        description="Remaining time at the current usage rate and credit.", default=None
    )
    unit: str | None = Field(description="Time unit type.", default=None)


class ResourcesModel(_base.ResourceModel):
    """Cherry Servers team credit resource detail model.

    This model is frozen by default,
    since it represents an actual Cherry Servers teams credit resources state.
    Here, resources refers to infrastructure objects that have a real cost.

    Attributes:
        pricing (cherry.plans.PricingModel | None): Team resource pricing data.
        remaining (cherry.teams.RemainingTimeModel | None):
         Team resource remaining time data.

    """

    pricing: PricingModel | None = Field(
        description="Team resource pricing data.", default=None
    )
    remaining: RemainingTimeModel | None = Field(
        description="Team resource remaining time data.", default=None
    )


class CreditDetailsModel(_base.ResourceModel):
    """Cherry Servers team credit details model.

    This model is frozen by default,
    since it represents an actual Cherry Servers team credit detail resource state.

    Attributes:
        remaining (float | None): Remaining credit.
        usage (float | None): Credit usage rate.
        currency (str | None): Credit currency.

    """

    remaining: float | None = Field(description="Remaining credit.", default=None)
    usage: float | None = Field(description="Credit usage rate.", default=None)
    currency: str | None = Field(description="Credit currency.", default=None)


class CreditModel(_base.ResourceModel):
    """Cherry Servers team credit model.

    This model is frozen by default,
    since in represents an actual Cherry Servers team credit resource state.

    Attributes:
        account (cherry.teams.CreditDetailsModel | None): Account credit details.
        promo (cherry.teams.CreditDetailsModel | None): Promotional credit details.
        resources (cherry.teams.ResourcesModel | None): Resources credit details.

    """

    account: CreditDetailsModel | None = Field(
        description="Account credit details.", default=None
    )
    promo: CreditDetailsModel | None = Field(
        description="Promotional credit details.", default=None
    )
    resources: ResourcesModel | None = Field(
        description="Resources credit details.", default=None
    )


class VatModel(_base.ResourceModel):
    """Cherry Servers team VAT model.

    This model is frozen by default,
    since it represents an actual Cherry Servers team VAT resource state.

    Attributes:
        amount (int | None): VAT rate.
        number (str | None): Amount of paid VAT.
        valid (bool | None): Whether VAT has been applied.

    """

    amount: int | None = Field(description="VAT rate.", default=None)
    number: str | None = Field(description="Amount of paid VAT.", default=None)
    valid: bool | None = Field(
        description="Whether VAT has been applied.", default=None
    )


class BillingModel(_base.ResourceModel):
    """Cherry Servers team billing model.

    This model is frozen by default,
    since it represents an actual Cherry Servers team billing resource state.

    Attributes:
        type (str | None): Billing type: `personal` or `business`.
        company_name (str | None): Company name, if applicable.
        company_code (str | None): Company code, if applicable.
        first_name (str | None): First name, if applicable.
        last_name (str | None): Last name, if applicable.
        address_1 (str | None): First address line, if applicable.
        address_2 (str | None): Last address line, if applicable.
        country_iso_2 (str | None): Country code, if applicable.
        city (str | None): City, if applicable.
        vat (cherry.teams.VatModel | None): VAT data.
        currency (str | None): Currency type.

    """

    type: str | None = Field(
        description="Billing type: `personal` or `business`.", default=None
    )
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
    vat: VatModel | None = Field(description="VAT data.", default=None)
    currency: str | None = Field(description="Currency type.", default=None)


class TeamModel(_base.ResourceModel):
    """Cherry Servers team model.

    This model is frozen by default,
    since it represents an actual Cherry Servers team resource state.

    Attributes:
        id (int): Team ID.
        name (str | None): Team name.
        credit (cherry.teams.CreditModel | None): Team credit data.
        billing (cherry.teams.BillingModel | None): Team billing data.
        href (str | None): Team href.

    """

    id: int = Field(description="Team ID.")
    name: str | None = Field(description="Team name.", default=None)
    credit: CreditModel | None = Field(description="Team credit data.", default=None)
    billing: BillingModel | None = Field(description="Team billing data.", default=None)
    href: str | None = Field(description="Team href.", default=None)


class CreationRequest(_base.RequestSchema):
    """Cherry Servers team creation request schema.

    Attributes:
        name (str): The name of the team. Required.
        type (str): Team type. Required. Defaults to `personal`.
        currency (str | None): Currency type.

    """

    name: str = Field(description="The name of the team. Required.")
    type: str = Field(
        description="Team type. Required. Defaults to `personal`.", default="personal"
    )
    currency: str | None = Field(description="Currency type.", default=None)


class UpdateRequest(_base.RequestSchema):
    """Cherry Servers team update request schema.

    Attributes:
        name (str | None): The name of the team.
        type (str | None): Team type.
        currency (str | None): Currency type.

    """

    name: str | None = Field(description="The name of the team.", default=None)
    type: str | None = Field(description="Team type.", default=None)
    currency: str | None = Field(description="Currency type.", default=None)


class TeamClient(_base.ResourceClient):
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
            create_req = cherry.teams.CreationRequest(
                name="python-sdk-test", currency="EUR"
            )
            new_team = facade.teams.create(create_req)

            # Update team.
            update_req = cherry.teams.UpdateRequest(
                name="python-sdk-test-updated"
            )
            new_team.update(update_req)

            # Delete team.
            new_team.delete()

    """

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

    def create(self, creation_schema: CreationRequest) -> Team:
        """Create a new team."""
        response = self._api_client.post("teams", creation_schema, None, 15)
        return self.get_by_id(response.json()["id"])

    def delete(self, team_id: int) -> None:
        """Delete a team by ID."""
        self._api_client.delete(f"teams/{team_id}", None, 5)

    def update(self, team_id: int, update_schema: UpdateRequest) -> Team:
        """Update a team by ID."""
        response = self._api_client.put(f"teams/{team_id}", update_schema, None, 10)
        return self.get_by_id(response.json()["id"])


class Team(_base.Resource[TeamClient, TeamModel]):
    """Cherry Servers team resource.

    This class represents an existing Cherry Servers resource
    and should only be initialized by :class:`TeamClient`.
    """

    def delete(self) -> None:
        """Delete Cherry Servers team resource."""
        self._client.delete(self._model.id)

    def update(self, update_schema: UpdateRequest) -> None:
        """Update Cherry Servers team resource."""
        updated = self._client.update(self._model.id, update_schema)
        self._model = updated.get_model()

    def get_id(self) -> int:
        """Get resource ID."""
        return self._model.id

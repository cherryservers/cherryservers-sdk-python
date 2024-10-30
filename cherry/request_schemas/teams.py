"""Cherry Servers team API request schemas."""

from __future__ import annotations

from pydantic import Field

from cherry.request_schemas import base


class CreationRequest(base.CherryRequestSchema):
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


class UpdateRequest(base.CherryRequestSchema):
    """Cherry Servers team update request schema.

    Attributes:
        name (str | None): The name of the team.
        type (str | None): Team type.
        currency (str | None): Currency type.

    """

    name: str | None = Field(description="The name of the team.", default=None)
    type: str | None = Field(description="Team type.", default=None)
    currency: str | None = Field(description="Currency type.", default=None)

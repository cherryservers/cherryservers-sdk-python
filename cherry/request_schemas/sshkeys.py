"""Cherry Servers SSH key API request schemas."""

from __future__ import annotations

from pydantic import Field

from cherry.request_schemas import base


class CreationRequest(base.CherryRequestSchema):
    """Cherry Servers SSH key creation request schema.

    Attributes:
        label (str): SSH key label.
        key (str): Public SSH key.

    """

    label: str = Field(description="SSH key label.")
    key: str = Field(description="Public SSH key.")


class UpdateRequest(base.CherryRequestSchema):
    """Cherry Servers SSH key update request schema.

    Attributes:
        label (str | None): SSH key label.
        key (str | None): Public SSH key.

    """

    label: str | None = Field(description="SSH key label.", default=None)
    key: str | None = Field(description="Public SSH key.", default=None)

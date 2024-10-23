"""Cherry Servers SSH key API request schemas."""

from __future__ import annotations

from pydantic import Field

from cherry.request_schemas import base


class Creation(base.CherryRequestSchema):
    """Cherry Servers SSH key creation request schema.

    Attributes:
        label (str): SSH key label.
        key (str): Public SSH key.

    """

    label: str = Field(description="SSH key label.")
    key: str = Field(description="Public SSH key.")

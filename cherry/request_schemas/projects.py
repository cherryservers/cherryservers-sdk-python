"""Cherry Servers project API request schemas."""

from __future__ import annotations

from pydantic import Field

from cherry.request_schemas import base


class CreationRequest(base.CherryRequestSchema):
    """Cherry Servers project creation request schema.

    Attributes:
        name (str): Project name.
        bgp (bool): Whether BGP is enabled for the project. Defaults to False.

    """

    name: str = Field(description="Project name.")
    bgp: bool = Field(
        description="Whether BGP is enabled for the project. Defaults to False.",
        default=False,
    )


class UpdateRequest(base.CherryRequestSchema):
    """Cherry Servers project update request schema.

    Attributes:
        name (str | None): Project name.
        bgp (bool | None): Whether BGP is enabled for the project..

    """

    name: str | None = Field(description="Project name.", default=None)
    bgp: bool | None = Field(
        description="Whether BGP is enabled for the project.", default=None
    )

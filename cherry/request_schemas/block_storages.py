"""Cherry Servers block storage API request schemas."""

from __future__ import annotations

from pydantic import Field

from cherry.request_schemas import base


class CreationRequest(base.CherryRequestSchema):
    """Cherry Servers block storage creation request schema.

    Attributes:
        region (str):  Region slug. Required.
        size (int):  Block storage size in GB. Required.
        description (str | None):  Block storage description.

    """

    region: str = Field(description="Region slug. Required.")
    size: int = Field(description="Block storage size in GB. Required.")
    description: str | None = Field(
        description="Block storage description.", default=None
    )


class UpdateRequest(base.CherryRequestSchema):
    """Cherry Servers block storage update request schema.

    Attributes:
        size (int | None): Block storage size in GB. Storage size cannot be reduced.
        description (str | None): Block storage description.

    """

    size: int | None = Field(
        description="Block storage size in GB. Storage size cannot be reduced",
        default=None,
    )
    description: str | None = Field(
        description="Block storage description.", default=None
    )


class AttachRequest(base.CherryRequestSchema):
    """Cherry Servers block storage server attachment request schema.

    Attributes:
        attach_to (int): ID of the server, to which the storage will be attached.

    """

    attach_to: int = Field(
        description="ID of the server, to which the storage will be attached."
    )

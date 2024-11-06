"""Cherry Servers backup storage API request schemas."""

from __future__ import annotations

from pydantic import Field

from cherry.request_schemas import base


class CreationRequest(base.CherryRequestSchema):
    """Cherry Servers backup storage creation request schema.

    Attributes:
        region (str):  Region slug. Required.
        slug (str):  Backup storage plan slug. Required.
        ssh_key (str | None):  Public SSH key for storage access.

    """

    region: str = Field(description="Region slug. Required.")
    slug: str = Field(description="Backup storage plan slug. Required.")
    ssh_key: str | None = Field(
        description="Public SSH key for storage access.", default=None
    )


class UpdateRequest(base.CherryRequestSchema):
    """Cherry Servers backup storage update request schema.

    Attributes:
        slug (str | None):  Backup storage plan slug.
        password (str | None): Password for backup storage access.
        ssh_key (str | None):  Public SSH key for storage access.

    """

    slug: str | None = Field(description="Backup storage plan slug.", default=None)
    password: str | None = Field(
        description="Password for backup storage access.", default=None
    )
    ssh_key: str | None = Field(
        description="Public SSH key for storage access.", default=None
    )


class UpdateAccessMethodsRequest(base.CherryRequestSchema):
    """Cherry Servers backup storage update access methods request schema.

    Attributes:
        enabled (bool | None):  Enable/Disable backup storage access methods.
        whitelist (list[str] | None): List of whitelisted IP addresses.
        ssh_key (str | None):  Public SSH key for storage access.

    """

    enabled: bool | None = Field(
        description="Enable/Disable backup storage access methods.", default=None
    )
    whitelist: list[str] | None = Field(
        description="List of  whitelisted IP addresses.", default=None
    )
    ssh_key: str | None = Field(
        description="Public SSH key for storage access.", default=None
    )

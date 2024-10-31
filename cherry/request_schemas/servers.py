"""Cherry Servers server API request schemas."""

from __future__ import annotations

from pydantic import Field

from cherry.request_schemas import base


class CreationRequest(base.CherryRequestSchema):
    """Cherry Servers server creation request schema.

    Attributes:
        plan (str): Plan slug. Required.
        image (str | None): Image slug.
        os_partition_size (int | None): OS partition size.
        region (str): Region slug. Required.
        hostname (str | None): Server hostname.
         Can be used to identify servers in most contexts.
        ssh_keys (Set[int] | None): IDs of SSH keys that will be added to the server.
        ip_addresses (Set[str] | None):
         IDs of extra IP addresses that will be attached to the server.
        user_data (str | None): Base64 encoded user-data blob.
         Either a bash or cloud-config script.
        tags (dict[str, str] | None): User-defined server tags.
        spot_market (bool): Whether the server should be a spot instance.
         Defaults to False.
        storage_id (int | None): ID of the EBS that will be attached to the server.

    """

    plan: str = Field(description="Plan slug. Required.")
    image: str | None = Field(description="Image slug.", default=None)
    os_partition_size: int | None = Field(
        description="OS partition size.", default=None
    )
    region: str = Field(description="Region slug. Required.")
    hostname: str | None = Field(
        description="Server hostname."
        "Can be used to identify servers in most contexts.",
        default=None,
    )
    ssh_keys: set[int] | None = Field(
        description="IDs of the SSH keys that will be added to the server.",
        default=None,
    )
    ip_addresses: set[str] | None = Field(
        description="IDs of extra IP addresses that will be attached to the server.",
        default=None,
    )
    user_data: str | None = Field(
        description="Base64 encoded user-data blob. Either a bash or cloud-config script.",
        default=None,
    )
    tags: dict[str, str] | None = Field(
        description="User-defined server tags.", default=None
    )
    spot_market: bool = Field(
        description="Whether the server should be a spot instance. Defaults to False.",
        default=False,
    )
    storage_id: int | None = Field(
        description="ID of the EBS that will be attached to the server.", default=None
    )


class UpdateRequest(base.CherryRequestSchema):
    """Cherry Servers server update request schema.

    Attributes:
        name (str | None): Server name.
        hostname (str | None): Server hostname.
        tags (dict[str, str] | None): User-defined server tags.
        bgp (bool | None): Whether the server should have BGP enabled.

    """

    name: str | None = Field(description="Server name.", default=None)
    hostname: str | None = Field(description="Server hostname.", default=None)
    tags: dict[str, str] | None = Field(
        description="User-defined server tags.", default=None
    )
    bgp: bool | None = Field(
        description="Whether the server should have BGP enabled.", default=None
    )


class PowerOffRequest(base.CherryRequestSchema):
    """Cherry Servers server power off request schema."""

    type: str = "power-off"


class PowerOnRequest(base.CherryRequestSchema):
    """Cherry Servers server power on request schema."""

    type: str = "power-on"


class RebootRequest(base.CherryRequestSchema):
    """Cherry Servers server reboot request schema."""

    type: str = "reboot"


class EnterRescueModeRequest(base.CherryRequestSchema):
    """Cherry Servers server enter rescue mode request schema.

    Attributes:
        password (str):
         The password that the server will have while in rescue mode. Required.

    """

    type: str = "enter-rescue-mode"
    password: str = Field(
        description="The password that the server will have while in rescue mode. Required.",
    )


class ExitRescueModeRequest(base.CherryRequestSchema):
    """Cherry Servers server exit rescue mode request schema."""

    type: str = "exit-rescue-mode"


class ResetBMCPasswordRequest(base.CherryRequestSchema):
    """Cherry Servers server reset BMC password request schema."""

    type: str = "reset-bmc-password"


class RebuildRequest(base.CherryRequestSchema):
    """Cherry Servers server rebuild request schema.

    Attributes:
        image (str | None): Image slug.
        hostname (str): Server hostname. Required.
        password (str): Server root user password. Required
        ssh_keys (Set[int] | None):
         IDs of SSH keys that will be added to the server.
        user_data (str | None): Base64 encoded user-data blob.
         Either a bash or cloud-config script.
        os_partition_size (int | None): OS partition size in GB.

    """

    type: str = "rebuild"
    image: str | None = Field(description="Image slug.", default=None)
    hostname: str = Field(description="Server hostname.")
    password: str = Field(description="Server root user password.")
    ssh_keys: set[int] | None = Field(
        description="IDs of SSH keys that will be added to the server.", default=None
    )
    user_data: str | None = Field(
        description="Base64 encoded user-data blob. Either a bash or cloud-config script.",
        default=None,
    )
    os_partition_size: int | None = Field(
        description="OS partition size.", default=None
    )

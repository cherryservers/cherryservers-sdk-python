"""Cherry Servers IP address API request schemas."""

from __future__ import annotations

from pydantic import Field

from cherry.request_schemas import base


class CreationRequest(base.CherryRequestSchema):
    """Cherry Servers IP address creation request schema.

    Attributes:
        region (str): IP address region slug. Required.
        routed_to (str | None):
         ID of the IP address that the created address will be routed to.
         Mutually exclusive with `targeted_to`.
        targeted_to (int | None):
         ID of the server that the created address will be targeted to.
         Mutually exclusive with `routed_to`.
        ptr_record (str | None): IP address PTR record.
        a_record (str | None): IP address A record.
        ddos_scrubbing (bool):
         Whether DDoS scrubbing should be enabled for this IP address.
         Disabled by default.
        tags (dict[str, str] | None): User-defined IP address tags.

    """

    region: str = Field(description="IP address region slug. Required.")
    routed_to: str | None = Field(
        description="ID of the IP address that the created address will be routed to."
        " Mutually exclusive with `targeted_to`. Optional.",
        default=None,
    )
    targeted_to: int | None = Field(
        description="ID of the server that the created address will be targeted to."
        " Mutually exclusive with `routed_to`.",
        default=None,
    )
    ptr_record: str | None = Field(description="IP address PTR record.", default=None)
    a_record: str | None = Field(description="IP address A record.", default=None)
    ddos_scrubbing: bool = Field(
        description="Whether DDoS scrubbing should be enabled for this IP address."
        "Disabled by default.",
        default=False,
    )
    tags: dict[str, str] | None = Field(
        description="User-defined IP address tags.", default=None
    )


class UpdateRequest(base.CherryRequestSchema):
    """Cherry Servers IP address update request schema.

    Attributes:
        ptr_record (str | None): IP address PTR record.
        a_record (str | None): IP address A record.
        routed_to (str | None):
         ID of the IP address that this address will be routed to.
         Mutually exclusive with `targeted_to`.
        targeted_to (int | None):
         ID of the server that this address will be targeted to.
         Mutually exclusive with `routed_to`.
         Set to 0 to unassign IP address from server.
        tags (dict[str, str] | None): User-defined IP address tags.

    """

    ptr_record: str | None = Field(description="IP address PTR record.", default=None)
    a_record: str | None = Field(description="IP address A record.", default=None)
    routed_to: str | None = Field(
        description="ID of the IP address that this address will be routed to."
        " Mutually exclusive with `targeted_to`.",
        default=None,
    )
    targeted_to: int | None = Field(
        description="ID of the server that the address will be targeted to."
        " Mutually exclusive with `routed_to`."
        " Set to 0 to unassign IP address from server.",
        default=None,
    )
    tags: dict[str, str] | None = Field(
        description="User-defined IP address tags.", default=None
    )

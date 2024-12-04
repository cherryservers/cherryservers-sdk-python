"""Cherry Servers IP address resource management module."""

from __future__ import annotations

from pydantic import Field

from cherry import _base, projects, regions


class AddressAttachedError(Exception):
    """Attempted operation forbidden for attached IP addresses."""

    def __init__(self, msg: str) -> None:
        """Initialize error."""
        super().__init__(msg)


class AttachedServerModel(_base.ResourceModel):
    """Cherry Servers attached server model.

    This model is frozen by default,
    since it represents an actual Cherry Servers server
    resource.

    This is a minimal server model meant for other resource models
    than contain a server. Avoids circular references.

    Attributes:
        id (int): Server ID. Non-existent server will have value `0`.
        href (str | None): Server href.
        hostname (str | None): Server hostname.
         Can be used to identify servers in most contexts.

    """

    id: int = Field(description="Server ID.")
    href: str | None = Field(description="Server href.", default=None)
    hostname: str | None = Field(
        description="Server hostname. Can be used to identify servers in most contexts.",
        default=None,
    )


class IPModel(_base.ResourceModel):
    """Cherry Servers IP address model.

    This model is frozen by default,
    since it represents an actual Cherry Servers IP address resource state.

    Attributes:
        id (int): IP address ID.
        address (str | None): IP address.
        address_family (str | None): IP address family, such as 4 or 6.
        cidr (str | None): IP address CIDR.
        gateway (str | None): IP address gateway address, if applicable.
        type (str | None): IP address type, such as `floating-ip` or `primary-ip`.
        region (cherry.regions.RegionModel | None): IP address region.
        routed_to (cherry.ips.IPModel | None):
         IP address that this address is routed, if applicable.
        targeted_to (cherry.ips.AttachedServerModel | None):
         Server that this address is targeted to, if applicable.
        project (cherry.projects.ProjectModel | None):
         The project that the IP address belongs to.
        ptr_record (str | None): IP address PTR record, if applicable.
        a_record (str | None): IP address A record, if applicable.
        tags (dict[str, str] | None): IP address user-defined tags.
        href (str | None): IP address href.

    """

    id: str = Field(description="IP address ID.")
    address: str | None = Field(description="IP address.", default=None)
    address_family: int | None = Field(
        description="IP address family, such as 4 or 6.", default=None
    )
    cidr: str | None = Field(description="IP address CIDR.", default=None)
    gateway: str | None = Field(
        description="IP address gateway address, if applicable.", default=None
    )
    type: str | None = Field(
        description="IP address type, such as floating-ip or primary-ip.", default=None
    )
    region: regions.RegionModel | None = Field(
        description="IP address region.", default=None
    )
    routed_to: IPModel | None = Field(
        description="IP address that this address is routed to, if applicable.",
        default=None,
    )
    targeted_to: AttachedServerModel | None = Field(
        description="Server that this address is targeted to, if applicable.",
        default=None,
    )

    project: projects.ProjectModel | None = Field(
        description=" Project that the IP address belongs to.", default=None
    )
    ptr_record: str | None = Field(
        description="IP address PTR record, if applicable.", default=None
    )
    a_record: str | None = Field(
        description="IP address A record, if applicable.", default=None
    )
    tags: dict[str, str] | None = Field(
        description="IP address user-defined tags.", default=None
    )
    href: str | None = Field(description="IP address href.", default=None)


class CreationRequest(_base.RequestSchema):
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
    tags: dict[str, str] | None = Field(
        description="User-defined IP address tags.", default=None
    )


class UpdateRequest(_base.RequestSchema):
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


class IPClient(_base.ResourceClient):
    """Cherry Servers IP address client.

    Manage Cherry Servers IP address resources.
    This class should typically be initialized by

    :class:`cherry.facade.CherryApiFacade`.

    Example:
        .. code-block:: python

            facade = cherry.facade.CherryApiFacade(token="my-token")

            # Get IP address by id.
            ip = facade.ips.get_by_id("c8b0cb54-cbd6-a90f-d291-769b6db0f1b9")

            # List all project IPs.
            ips = facade.ips.get_by_project(123456)

            # Create an IP address.
            creation_req = cherry.ips.CreationRequest(
                region="eu_nord_1",
                ptr_record="test",
                a_record="test",
                targeted_to=606764,
                tags={"env": "test"},
            )
            fip = facade.ips.create(creation_req, project_id=123456)

            # Update IP address.
            update_req = cherry.ips.UpdateRequest(
                ptr_record="",
                a_record="",
            )
            fip.update(update_req)

            # Delete IP address.
            fip.delete()

    """

    def get_by_id(self, ip_id: str) -> IP:
        """Retrieve a IP address by ID."""
        response = self._api_client.get(
            f"ips/{ip_id}",
            {"fields": "ip,project,routed_to,region,href,bgp,id,hostname"},
            10,
        )
        ip_model = IPModel.model_validate(response.json())
        return IP(self, ip_model)

    def get_by_project(self, project_id: int) -> list[IP]:
        """Retrieve all IPs that belong to a specified project."""
        response = self._api_client.get(
            f"projects/{project_id}/ips",
            {"fields": "ip,project,routed_to,region,href,bgp,id,hostname"},
            10,
        )
        ips: list[IP] = []
        for value in response.json():
            ip_model = IPModel.model_validate(value)
            ips.append(IP(self, ip_model))

        return ips

    def create(self, creation_schema: CreationRequest, project_id: int) -> IP:
        """Create a new IP address."""
        response = self._api_client.post(
            f"projects/{project_id}/ips", creation_schema, None, 30
        )
        return self.get_by_id(response.json()["id"])

    def delete(self, ip_id: str) -> None:
        """Delete IP address by ID."""
        self._api_client.delete(f"ips/{ip_id}", None, 10)

    def update(self, ip_id: str, update_schema: UpdateRequest) -> IP:
        """Update IP address by ID."""
        response = self._api_client.put(f"ips/{ip_id}", update_schema, None, 30)
        return self.get_by_id(response.json()["id"])


class IP(_base.Resource[IPClient, IPModel]):
    """Cherry Servers IP address resource.

    This class represents an existing Cherry Servers resource
    and should only be initialized by :class:`IPClient`.
    """

    def delete(self) -> None:
        """Delete Cherry Servers IP address resource."""
        if self._model.routed_to:
            msg = "Attached IP address cannot be deleted."
            raise AddressAttachedError(msg)
        self._client.delete(self._model.id)

    def update(self, update_schema: UpdateRequest) -> None:
        """Update Cherry Servers IP address resource."""
        updated = self._client.update(self._model.id, update_schema)
        self._model = updated._model  # noqa: SLF001

    def get_id(self) -> str:
        """Get resource ID."""
        return self._model.id

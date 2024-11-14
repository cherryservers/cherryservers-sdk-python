"""Cherry Servers server resource management module."""

from __future__ import annotations

from pydantic import Field

from cherry import _client, _models
from cherry.block_storages import BlockStorageModel
from cherry.ips import IPModel
from cherry.plans import PlanModel, PricingModel
from cherry.projects import ProjectModel
from cherry.regions import RegionModel
from cherry.sshkeys import SSHKeyModel


class NotBaremetalError(Exception):
    """Attempted baremetal only operation on VPS."""

    def __init__(self) -> None:
        """Initialize error."""
        super().__init__("Only baremetal servers can enter rescue mode.")


class ServerBGPRouteModel(_models.DefaultModel):
    """Cherry Servers server BGP route model.

    This model is frozen by default,
    since it represents an actual Cherry Servers
    server BGP route resource state.

    Attributes:
        subnet (str | None): BGP route subnet.
        active (bool | None): Whether the BGP route is active.
        router (str | None): BGP router address.
        age (str | None): BGP route age.
        updated (str | None): Date of last update.

    """

    subnet: str | None = Field(description="BGP route subnet.", default=None)
    active: bool | None = Field(
        description="Whether the BGP route is active.", default=None
    )
    router: str | None = Field(description="BGP router address.", default=None)
    age: str | None = Field(description="BGP route age.", default=None)
    updated: str | None = Field(description="Date of last update.", default=None)


class ServerBGPModel(_models.DefaultModel):
    """Cherry Servers server BGP model.

    This model is frozen by default,
    since it represents an actual Cherry Servers
    server BGP resource state.

    Attributes:
        enabled (bool | None): Whether BGP is enabled.
        available (bool | None): Whether BGP is available.
        status (str | None): BGP status.
        routers (int | None): BGP routers.
        connected (int | None): BGP connections.
        limit (int | None): BGP limit.
        active (int | None): BGP active.
        routes (list[cherry.servers.ServerBGPRouteModel] | None): BGP routes.
        updated (str | None): Date of last update.

    """

    enabled: bool | None = Field(description="Whether BGP is enabled.", default=None)
    available: bool | None = Field(
        description="Whether BGP is available.", default=None
    )
    status: str | None = Field(description="BGP status.", default=None)
    routers: int | None = Field(description="BGP routers.", default=None)
    connected: int | None = Field(description="BGP connections.", default=None)
    limit: int | None = Field(description="BGP limit.", default=None)
    active: bool | None = Field(description="BGP active.", default=None)
    routes: list[ServerBGPRouteModel] | None = Field(
        description="BGP routes.", default=None
    )
    updated: str | None = Field(description="Date of last update.", default=None)


class ServerDeployedImageModel(_models.DefaultModel):
    """Cherry Servers server deployed image model.

    This model is frozen by default,
    since it represents an actual Cherry Servers
    server deployed image resource state.

    Attributes:
        name (str | None): Full name of the deployed image.
        slug (str | None): Slug of the deployed image name.

    """

    name: str | None = Field(
        description="Full name of the deployed image.", default=None
    )
    slug: str | None = Field(
        description="Slug of the deployed image name.", default=None
    )


class ServerBMCModel(_models.DefaultModel):
    """Cherry Servers server BMC model.

    This model is frozen by default,
    since it represents an actual Cherry Servers
    server BMC resource state.

    Attributes:
        password (str | None): Server BMC password. Scrubbed at 24 hours after creation.
        user (str | None): Server BMC username. Scrubbed at 24 hours after creation.

    """

    password: str | None = Field(
        description="Server BMC password. Scrubbed at 24 hours after creation.",
        default=None,
    )
    user: str | None = Field(
        description="Server BMC username. Scrubbed at 24 hours after creation.",
        default=None,
    )


class ServerModel(_models.DefaultModel):
    """Cherry Servers server model.

    This model is frozen by default,
    since it represents an actual Cherry Servers server resource state.

    Attributes:
        id (int): Server ID.
        name (str | None): Server name. Typically corresponds to plan name.
        href (str | None): Server href.
        bmc (cherry.servers.ServerBMCModel | None):
         Server BMC credential data. Only for baremetal servers.
         Scrubbed at 24 hours after creation.
        hostname (str | None): Server hostname.
        Can be used to identify servers in most contexts.
        password (str | None): Server user password. Scrubbed 24 hours after creation.
        username (str | None): Server user username. Scrubbed 24 hours after creation.
         deployed_image (cherry.servers.ServerDeployedImageModel | None): OS image data.
        spot_instance (bool | None): Whether the server belongs the spot market.
        region (cherry.regions.RegionModel | None): Region data.
        state (str | None): Server state.
        status (str | None): Server status.
        bgp (cherry.servers.ServerBGPModel | None): BGP data.
        plan (cherry.plans.PlanModel): Plan data.
        pricing (cherry.plans.PricingModel | None): Pricing data.
        ssh_keys (list[cherry.sshkeys.SSHKeyModel] | None): SSH key data.
        tags (dict[str, str] | None): User-defined server tags.
        termination_date (str | None): Server termination date.
        created_at (str | None): Server deployment date.
        traffic_used_bytes (int | None): Server traffic usage.
        project (cherry.projects.ProjectModel | None): Project data.
        ip_addresses (list[cherry.ips.IPModel] | None): Server IP address data.
        storage (cherry.block_storages.BlockStorageModel | None): Block storage data.

    """

    id: int = Field(description="Server ID.")
    name: str = Field(
        description="Server name. Typically corresponds to plan name.", default=None
    )
    href: str = Field(description="Server href.", default=None)
    bmc: ServerBMCModel | None = Field(
        description="Server BMC credential data. Only for baremetal servers."
        "Scrubbed at 24 hours after creation.",
        default=None,
    )
    hostname: str = Field(
        description="Server hostname. Can be used to identify servers in most contexts.",
        default=None,
    )
    password: str | None = Field(
        description="Server user password. Scrubbed at 24 hours after creation.",
        default=None,
    )
    username: str | None = Field(
        description="Server user username. Scrubbed at 24 hours after creation.",
        default=None,
    )
    deployed_image: ServerDeployedImageModel | None = Field(
        description="OS image data.", default=None
    )
    spot_instance: bool | None = Field(
        description="Whether the server belongs the spot market.", default=None
    )
    region: RegionModel | None = Field(description="Region data.", default=None)
    state: str | None = Field(description="Server state.", default=None)
    status: str | None = Field(description="Server status.", default=None)
    bgp: ServerBGPModel | None = Field(description="BGP data.", default=None)
    plan: PlanModel = Field(description="Plan data.")
    pricing: PricingModel | None = Field(description="Pricing data.", default=None)
    ssh_keys: list[SSHKeyModel] | None = Field(
        description="SSH key data.", default=None
    )
    ip_addresses: list[IPModel] | None = Field(
        description="Server IP address data.", default=None
    )
    storage: BlockStorageModel | None = Field(
        description="Block storage data.", default=None
    )
    tags: dict[str, str] | None = Field(
        description="User-defined server tags.", default=None
    )
    termination_date: str | None = Field(
        description="Server termination date.", default=None
    )
    created_at: str | None = Field(description="Server deployment date.", default=None)
    traffic_used_bytes: int | None = Field(
        description="Server traffic usage.", default=None
    )
    project: ProjectModel | None = Field(description="Project data.", default=None)


class CreationRequest(_models.CherryRequestSchema):
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


class UpdateRequest(_models.CherryRequestSchema):
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


class PowerOffRequest(_models.CherryRequestSchema):
    """Cherry Servers server power off request schema."""

    type: str = "power-off"


class PowerOnRequest(_models.CherryRequestSchema):
    """Cherry Servers server power on request schema."""

    type: str = "power-on"


class RebootRequest(_models.CherryRequestSchema):
    """Cherry Servers server reboot request schema."""

    type: str = "reboot"


class EnterRescueModeRequest(_models.CherryRequestSchema):
    """Cherry Servers server enter rescue mode request schema.

    Attributes:
        password (str):
         The password that the server will have while in rescue mode. Required.

    """

    type: str = "enter-rescue-mode"
    password: str = Field(
        description="The password that the server will have while in rescue mode. Required.",
    )


class ExitRescueModeRequest(_models.CherryRequestSchema):
    """Cherry Servers server exit rescue mode request schema."""

    type: str = "exit-rescue-mode"


class ResetBMCPasswordRequest(_models.CherryRequestSchema):
    """Cherry Servers server reset BMC password request schema."""

    type: str = "reset-bmc-password"


class RebuildRequest(_models.CherryRequestSchema):
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


class Server:
    """Cherry Servers Server resource.

    This class represents an existing Cherry Servers resource
    and should only be initialized by :class:`ServerClient`.

    Attributes:
        model (ServerModel): Cherry Servers server model.
            This is a Pydantic model that contains server data.
            A standard dictionary can be extracted with ``model.model_dump()``.

    """

    def __init__(self, client: ServerClient, model: ServerModel) -> None:
        """Initialize a Cherry Servers server resource."""
        self._client = client
        self.model = model

    def update(self, update_schema: UpdateRequest) -> None:
        """Update Cherry Servers server resource."""
        updated = self._client.update(self.model.id, update_schema)
        self.model = updated.model

    def delete(self) -> None:
        """Delete Cherry Servers server resource."""
        self._client.delete(self.model.id)

    def power_off(self) -> None:
        """Power off Cherry Servers server."""
        serv = self._client.power_off(self.model.id)
        self.model = serv.model

    def power_on(self) -> None:
        """Power on Cherry Servers server."""
        serv = self._client.power_on(self.model.id)
        self.model = serv.model

    def reboot(self) -> None:
        """Reboot a Cherry Servers server."""
        serv = self._client.reboot(self.model.id)
        self.model = serv.model

    def enter_rescue_mode(self, rescue_mode_schema: EnterRescueModeRequest) -> None:
        """Put a Cherry Servers server into rescue mode.

        Only for baremetal servers!
        """
        serv = self._client.enter_rescue_mode(self.model.id, rescue_mode_schema)
        self.model = serv.model

    def exit_rescue_mode(self) -> None:
        """Put a Cherry Servers server out of rescue mode."""
        serv = self._client.exit_rescue_mode(self.model.id)
        self.model = serv.model

    def rebuild(self, rebuild_schema: RebuildRequest) -> None:
        """Rebuild a Cherry Servers server.

        WARNING: this a destructive action that will delete all of your data.
        """
        serv = self._client.rebuild(self.model.id, rebuild_schema)
        self.model = serv.model

    def reset_bmc_password(self) -> None:
        """Reset server BMC password.

        Only for baremetal servers!
        """
        serv = self._client.reset_bmc_password(self.model.id)
        self.model = serv.model


class ServerClient:
    """Cherry Servers server client.

    Manage Cherry Servers server resources.
    This class should typically be initialized by
    :class:`cherry.facade.CherryApiFacade`.

    Example:
        .. code-block:: python

            facade = cherry.facade.CherryApiFacade(token="my-token")

            # Get server by id.
            server = facade.servers.get_by_id(123456)

            # List all project servers.
            print("List of all project servers:")
            for server in facade.servers.get_by_project(123456):
                print(server.model)

            # Create a server.
            creation_req = cherry.servers.CreationRequest(
                region="eu_nord_1", plan="cloud_vps_1"
            )
            server = facade.servers.create(creation_req, project_id=217727)

            # Update server.
            update_req = cherry.servers.UpdateRequest(
                name="test", hostname="test", tags={"env": "test"}, bgp=True
            )
            server.update(update_req)

            # Delete server.
            server.delete()

    """

    def __init__(self, api_client: _client.CherryApiClient) -> None:
        """Initialize a Cherry Servers server client."""
        self._api_client = api_client

    def get_by_id(self, server_id: int) -> Server:
        """Retrieve a server by ID."""
        response = self._api_client.get(
            f"servers/{server_id}",
            None,
            10,
        )
        server_model = ServerModel.model_validate(response.json())
        return Server(self, server_model)

    def get_by_project(self, project_id: int) -> list[Server]:
        """Retrieve all servers that belong to a specified project."""
        response = self._api_client.get(
            f"projects/{project_id}/servers",
            None,
            10,
        )
        servers: list[Server] = []
        for value in response.json():
            server_model = ServerModel.model_validate(value)
            servers.append(Server(self, server_model))

        return servers

    def create(self, creation_schema: CreationRequest, project_id: int) -> Server:
        """Create a new server."""
        response = self._api_client.post(
            f"projects/{project_id}/servers", creation_schema, None, 30
        )
        return self.get_by_id(response.json()["id"])

    def delete(self, server_id: int) -> None:
        """Delete server by ID."""
        self._api_client.delete(f"servers/{server_id}", None, 20)

    def update(self, server_id: int, update_schema: UpdateRequest) -> Server:
        """Update server by ID."""
        response = self._api_client.put(f"servers/{server_id}", update_schema, None, 30)
        return self.get_by_id(response.json()["id"])

    def power_off(self, server_id: int) -> Server:
        """Power off server by ID."""
        response = self._api_client.post(
            f"servers/{server_id}/actions",
            PowerOffRequest(),
            None,
            30,
        )
        return self.get_by_id(response.json()["id"])

    def power_on(self, server_id: int) -> Server:
        """Power on server by ID."""
        response = self._api_client.post(
            f"servers/{server_id}/actions",
            PowerOnRequest(),
            None,
            30,
        )
        return self.get_by_id(response.json()["id"])

    def reboot(self, server_id: int) -> Server:
        """Reboot server by ID."""
        response = self._api_client.post(
            f"servers/{server_id}/actions",
            RebootRequest(),
            None,
            30,
        )
        return self.get_by_id(response.json()["id"])

    def enter_rescue_mode(
        self,
        server_id: int,
        rescue_mode_schema: EnterRescueModeRequest,
    ) -> Server:
        """Put server into rescue mode.

        Only for baremetal servers!
        """
        server = self.get_by_id(server_id)

        if server.model.plan.type != "baremetal":
            raise NotBaremetalError

        response = self._api_client.post(
            f"servers/{server_id}/actions",
            rescue_mode_schema,
            None,
            30,
        )

        return self.get_by_id(response.json()["id"])

    def exit_rescue_mode(self, server_id: int) -> Server:
        """Put server out of rescue mode."""
        response = self._api_client.post(
            f"servers/{server_id}/actions",
            ExitRescueModeRequest(),
            None,
            30,
        )

        return self.get_by_id(response.json()["id"])

    def rebuild(self, server_id: int, rebuild_schema: RebuildRequest) -> Server:
        """Rebuild server.

        WARNING: this a destructive action that will delete all of your data.
        """
        response = self._api_client.post(
            f"servers/{server_id}/actions",
            rebuild_schema,
            None,
            30,
        )

        return self.get_by_id(response.json()["id"])

    def reset_bmc_password(self, server_id: int) -> Server:
        """Reset server BMC password.

        Only for baremetal servers!
        """
        server = self.get_by_id(server_id)

        if server.model.plan.type != "baremetal":
            raise NotBaremetalError

        response = self._api_client.post(
            f"servers/{server_id}/actions",
            ResetBMCPasswordRequest(),
            None,
            30,
        )

        return self.get_by_id(response.json()["id"])

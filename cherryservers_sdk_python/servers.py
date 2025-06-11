"""Cherry Servers server resource management module."""

from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import Field

from cherryservers_sdk_python import (
    _base,
    _resource_polling,
    block_storages,
    ips,
    plans,
    projects,
    regions,
    sshkeys,
)

if TYPE_CHECKING:
    from requests import Response


class NotBaremetalError(Exception):
    """Attempted baremetal only operation on VPS."""

    def __init__(self) -> None:
        """Initialize error."""
        super().__init__("This operation can only be performed on bare-metal servers.")


class ServerBGPRouteModel(_base.ResourceModel):
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


class ServerBGPModel(_base.ResourceModel):
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
        routes (list[cherryservers_sdk_python.servers.ServerBGPRouteModel] | None):
         BGP routes.
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


class ServerDeployedImageModel(_base.ResourceModel):
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


class ServerBMCModel(_base.ResourceModel):
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


class ServerModel(_base.ResourceModel):
    """Cherry Servers server model.

    This model is frozen by default,
    since it represents an actual Cherry Servers server resource state.

    Attributes:
        id (int): Server ID.
        name (str | None): Server name. Typically corresponds to plan name.
        href (str | None): Server href.
        bmc (cherryservers_sdk_python.servers.ServerBMCModel | None):
         Server BMC credential data. Only for baremetal servers.
         Scrubbed at 24 hours after creation.
        hostname (str | None): Server hostname.
        password (str | None): Server user password. Scrubbed 24 hours after creation.
        username (str | None): Server user username. Scrubbed 24 hours after creation.
        deployed_image (cherryservers_sdk_python.servers.ServerDeployedImageModel | None):
         OS image data.
        spot_instance (bool | None): Whether the server belongs the spot market.
        region (cherryservers_sdk_python.regions.RegionModel | None): Region data.
        state (str | None): Server state.
        status (str): Server status.
        bgp (cherryservers_sdk_python.servers.ServerBGPModel | None): BGP data.
        plan (cherryservers_sdk_python.plans.PlanModel | None): Plan data.
        pricing (cherryservers_sdk_python.plans.PricingModel | None): Pricing data.
        ssh_keys (list[cherryservers_sdk_python.sshkeys.SSHKeyModel] | None): SSH key data.
        tags (dict[str, str] | None): User-defined server tags.
        termination_date (str | None): Server termination date.
        created_at (str | None): Server deployment date.
        traffic_used_bytes (int | None): Server traffic usage.
        project (cherryservers_sdk_python.projects.ProjectModel | None): Project data.
        ip_addresses (list[cherryservers_sdk_python.ips.IPModel] | None):
         Server IP address data.
        storage (cherryservers_sdk_python.block_storages.BlockStorageModel | None):
         Block storage data.

    """  # noqa: W505

    id: int = Field(description="Server ID.")
    name: str | None = Field(
        description="Server name. Typically corresponds to plan name.", default=None
    )
    href: str | None = Field(description="Server href.", default=None)
    bmc: ServerBMCModel | None = Field(
        description="Server BMC credential data. Only for baremetal servers."
        "Scrubbed at 24 hours after creation.",
        default=None,
    )
    hostname: str | None = Field(
        description="Server hostname.",
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
    region: regions.RegionModel | None = Field(description="Region data.", default=None)
    state: str | None = Field(description="Server state.", default=None)
    status: str = Field(description="Server status.")
    bgp: ServerBGPModel | None = Field(description="BGP data.", default=None)
    plan: plans.PlanModel | None = Field(description="Plan data.", default=None)
    pricing: plans.PricingModel | None = Field(
        description="Pricing data.", default=None
    )
    ssh_keys: list[sshkeys.SSHKeyModel] | None = Field(
        description="SSH key data.", default=None
    )
    ip_addresses: list[ips.IPModel] | None = Field(
        description="Server IP address data.", default=None
    )
    storage: block_storages.BlockStorageModel | None = Field(
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
    project: projects.ProjectModel | None = Field(
        description="Project data.", default=None
    )


class CreationRequest(_base.RequestSchema):
    """Cherry Servers server creation request schema.

    Attributes:
        plan (str): Plan slug. Required.
        image (str | None): Image slug.
        os_partition_size (int | None): OS partition size.
        region (str): Region slug. Required.
        hostname (str | None): Server hostname.
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
        description="Server hostname.",
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


class UpdateRequest(_base.RequestSchema):
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


class PowerOffRequest(_base.RequestSchema):
    """Cherry Servers server power off request schema."""

    type: str = "power-off"


class PowerOnRequest(_base.RequestSchema):
    """Cherry Servers server power on request schema."""

    type: str = "power-on"


class RebootRequest(_base.RequestSchema):
    """Cherry Servers server reboot request schema."""

    type: str = "reboot"


class EnterRescueModeRequest(_base.RequestSchema):
    """Cherry Servers server enter rescue mode request schema.

    Attributes:
        password (str):
         The password that the server will have while in rescue mode. Required.

    """

    type: str = "enter-rescue-mode"
    password: str = Field(
        description="The password that the server will have while in rescue mode. Required.",
    )


class ExitRescueModeRequest(_base.RequestSchema):
    """Cherry Servers server exit rescue mode request schema."""

    type: str = "exit-rescue-mode"


class ResetBMCPasswordRequest(_base.RequestSchema):
    """Cherry Servers server reset BMC password request schema."""

    type: str = "reset-bmc-password"


class RebuildRequest(_base.RequestSchema):
    """Cherry Servers server rebuild request schema.

    Attributes:
        image (str): Image slug.
        hostname (str): Server hostname. Required.
        password (str): Server root user password. Required
        ssh_keys (Set[int] | None):
         IDs of SSH keys that will be added to the server.
        user_data (str | None): Base64 encoded user-data blob.
         Either a bash or cloud-config script.
        os_partition_size (int | None): OS partition size in GB.

    """

    type: str = "rebuild"
    image: str = Field(description="Image slug.")
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


class ServerClient(_base.ResourceClient):
    """Cherry Servers server client.

    Manage Cherry Servers server resources.
    This class should typically be initialized by
    :class:`cherryservers_sdk_python.facade.CherryApiFacade`.

    Example:
        .. code-block:: python

            facade = cherryservers_sdk_python.facade.CherryApiFacade(token="my-token")

            # Get server by id.
            server = facade.servers.get_by_id(123456)

            # List all project servers.
            print("List of all project servers:")
            for server in facade.servers.get_by_project(123456):
                print(server.get_model())

            # Create a server.
            creation_req = cherryservers_sdk_python.servers.CreationRequest(
                region="LT-Siauliai", plan="B1-1-1gb-20s-shared"
            )
            server = facade.servers.create(creation_req, project_id=217727)

            # Update server.
            update_req = cherryservers_sdk_python.servers.UpdateRequest(
                name="test", hostname="test", tags={"env": "test"}, bgp=True
            )
            server.update(update_req)

            # Delete server.
            server.delete()

    """

    DEFAULT_DEPLOYMENT_TIMEOUT = 1800

    def _wait_for_status(
        self, response: Response, target_status: str, timeout: float
    ) -> Server:
        resp_json = response.json()
        server = Server(self, ServerModel.model_validate(resp_json))
        _resource_polling.wait_for_resource_condition(
            server, timeout, lambda: server.get_status() == target_status
        )
        return server

    def get_by_id(self, server_id: int) -> Server:
        """Retrieve a server by ID."""
        response = self._api_client.get(
            f"servers/{server_id}",
            None,
            self.request_timeout,
        )
        server_model = ServerModel.model_validate(response.json())
        return Server(self, server_model)

    def list_by_project(self, project_id: int) -> list[Server]:
        """Retrieve all servers that belong to a specified project."""
        response = self._api_client.get(
            f"projects/{project_id}/servers",
            None,
            self.request_timeout,
        )
        servers: list[Server] = []
        for value in response.json():
            server_model = ServerModel.model_validate(value)
            servers.append(Server(self, server_model))

        return servers

    def create(
        self,
        creation_schema: CreationRequest,
        project_id: int,
        *,
        wait_for_active: bool = True,
        deployment_timeout: int = DEFAULT_DEPLOYMENT_TIMEOUT,
    ) -> Server:
        """Create a new server."""
        response = self._api_client.post(
            f"projects/{project_id}/servers",
            creation_schema,
            None,
            self.request_timeout,
        )
        if wait_for_active:
            return self._wait_for_status(response, "deployed", deployment_timeout)
        return self.get_by_id(response.json()["id"])

    def delete(self, server_id: int) -> None:
        """Delete server by ID."""
        self._api_client.delete(f"servers/{server_id}", None, self.request_timeout)

    def update(
        self,
        server_id: int,
        update_schema: UpdateRequest,
    ) -> Server:
        """Update server by ID."""
        response = self._api_client.put(
            f"servers/{server_id}", update_schema, None, self.request_timeout
        )
        return self.get_by_id(response.json()["id"])

    def power_off(
        self,
        server_id: int,
        *,
        wait_for_active: bool = True,
        deployment_timeout: int = DEFAULT_DEPLOYMENT_TIMEOUT,
    ) -> Server:
        """Power off server by ID."""
        response = self._api_client.post(
            f"servers/{server_id}/actions",
            PowerOffRequest(),
            None,
            self.request_timeout,
        )
        if wait_for_active:
            return self._wait_for_status(response, "deployed", deployment_timeout)
        return self.get_by_id(response.json()["id"])

    def power_on(
        self,
        server_id: int,
        *,
        wait_for_active: bool = True,
        deployment_timeout: int = DEFAULT_DEPLOYMENT_TIMEOUT,
    ) -> Server:
        """Power on server by ID."""
        response = self._api_client.post(
            f"servers/{server_id}/actions",
            PowerOnRequest(),
            None,
            self.request_timeout,
        )
        if wait_for_active:
            return self._wait_for_status(response, "deployed", deployment_timeout)
        return self.get_by_id(response.json()["id"])

    def reboot(
        self,
        server_id: int,
        *,
        wait_for_active: bool = True,
        deployment_timeout: int = DEFAULT_DEPLOYMENT_TIMEOUT,
    ) -> Server:
        """Reboot server by ID."""
        response = self._api_client.post(
            f"servers/{server_id}/actions",
            RebootRequest(),
            None,
            self.request_timeout,
        )
        if wait_for_active:
            return self._wait_for_status(response, "deployed", deployment_timeout)
        return self.get_by_id(response.json()["id"])

    def enter_rescue_mode(
        self,
        server_id: int,
        rescue_mode_schema: EnterRescueModeRequest,
        *,
        wait_for_active: bool = True,
        deployment_timeout: int = DEFAULT_DEPLOYMENT_TIMEOUT,
    ) -> Server:
        """Put server into rescue mode.

        Only for baremetal servers!
        """
        server = self.get_by_id(server_id)
        server_model = server.get_model()

        if server_model.plan is not None and server_model.plan.type != "baremetal":
            raise NotBaremetalError

        response = self._api_client.post(
            f"servers/{server_id}/actions",
            rescue_mode_schema,
            None,
            self.request_timeout,
        )

        if wait_for_active:
            return self._wait_for_status(response, "rescue mode", deployment_timeout)
        return self.get_by_id(response.json()["id"])

    def exit_rescue_mode(
        self,
        server_id: int,
        *,
        wait_for_active: bool = True,
        deployment_timeout: int = DEFAULT_DEPLOYMENT_TIMEOUT,
    ) -> Server:
        """Put server out of rescue mode."""
        response = self._api_client.post(
            f"servers/{server_id}/actions",
            ExitRescueModeRequest(),
            None,
            self.request_timeout,
        )

        if wait_for_active:
            return self._wait_for_status(response, "deployed", deployment_timeout)
        return self.get_by_id(response.json()["id"])

    def rebuild(
        self,
        server_id: int,
        rebuild_schema: RebuildRequest,
        *,
        wait_for_active: bool = True,
        deployment_timeout: int = DEFAULT_DEPLOYMENT_TIMEOUT,
    ) -> Server:
        """Rebuild server.

        WARNING: this a destructive action that will delete all of your data.
        """
        response = self._api_client.post(
            f"servers/{server_id}/actions",
            rebuild_schema,
            None,
            self.request_timeout,
        )
        if wait_for_active:
            return self._wait_for_status(response, "deployed", deployment_timeout)
        return self.get_by_id(response.json()["id"])

    def reset_bmc_password(self, server_id: int) -> Server:
        """Reset server BMC password.

        Only for baremetal servers!
        """
        server = self.get_by_id(server_id)
        server_model = server.get_model()

        if server_model.plan is not None and server_model.plan.type != "baremetal":
            raise NotBaremetalError

        response = self._api_client.post(
            f"servers/{server_id}/actions",
            ResetBMCPasswordRequest(),
            None,
            self.request_timeout,
        )

        return self.get_by_id(response.json()["id"])


class Server(
    _base.Resource[ServerClient, ServerModel], _resource_polling.RefreshableResource
):
    """Cherry Servers Server resource.

    This class represents an existing Cherry Servers resource
    and should only be initialized by :class:`ServerClient`.
    """

    def __init__(self, client: ServerClient, model: ServerModel) -> None:
        """Initialize a Cherry Servers server resource."""
        super().__init__(client, model)
        self._deployment_timeout = client.DEFAULT_DEPLOYMENT_TIMEOUT

    @property
    def deployment_timeout(self) -> int:
        """Deployment timeout in seconds."""
        return self._deployment_timeout

    @deployment_timeout.setter
    def deployment_timeout(self, value: int) -> None:
        """Deployment timeout in seconds."""
        self._deployment_timeout = value

    def update(self, update_schema: UpdateRequest) -> None:
        """Update Cherry Servers server resource."""
        updated = self._client.update(self._model.id, update_schema)
        self._model = updated.get_model()

    def delete(self) -> None:
        """Delete Cherry Servers server resource."""
        self._client.delete(self._model.id)

    def power_off(self) -> None:
        """Power off Cherry Servers server."""
        serv = self._client.power_off(
            self._model.id, deployment_timeout=self.deployment_timeout
        )
        self._model = serv.get_model()

    def power_on(self) -> None:
        """Power on Cherry Servers server."""
        serv = self._client.power_on(
            self._model.id, deployment_timeout=self.deployment_timeout
        )
        self._model = serv.get_model()

    def reboot(self) -> None:
        """Reboot a Cherry Servers server."""
        serv = self._client.reboot(
            self._model.id, deployment_timeout=self.deployment_timeout
        )
        self._model = serv.get_model()

    def enter_rescue_mode(self, rescue_mode_schema: EnterRescueModeRequest) -> None:
        """Put a Cherry Servers server into rescue mode.

        Only for baremetal servers!
        """
        serv = self._client.enter_rescue_mode(
            self._model.id,
            rescue_mode_schema,
            deployment_timeout=self.deployment_timeout,
        )
        self._model = serv.get_model()

    def exit_rescue_mode(self) -> None:
        """Put a Cherry Servers server out of rescue mode."""
        serv = self._client.exit_rescue_mode(
            self._model.id, deployment_timeout=self.deployment_timeout
        )
        self._model = serv.get_model()

    def rebuild(self, rebuild_schema: RebuildRequest) -> None:
        """Rebuild a Cherry Servers server.

        WARNING: this a destructive action that will delete all of your data!
        """
        serv = self._client.rebuild(
            self._model.id, rebuild_schema, deployment_timeout=self.deployment_timeout
        )
        self._model = serv.get_model()

    def reset_bmc_password(self) -> None:
        """Reset server BMC password.

        Only for baremetal servers!
        """
        serv = self._client.reset_bmc_password(self._model.id)
        self._model = serv.get_model()

    def refresh(self) -> None:
        """Refresh the server.

        Refreshes server model to match the actual state.
        """
        self._model = self._client.get_by_id(self._model.id).get_model()

    def get_status(self) -> str:
        """Get server status."""
        return self._model.status

    def get_plan_slug(self) -> str:
        """Get server plan slug.

        :returns str: Server plan slug. If non-existent, returns an empty string.
        """
        if self._model.plan is not None and self._model.plan.slug is not None:
            return self._model.plan.slug
        return ""

    def get_id(self) -> int:
        """Get server ID."""
        return self._model.id

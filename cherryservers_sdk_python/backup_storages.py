"""Cherry Servers backup storage resource management module."""

from __future__ import annotations

from pydantic import Field

from cherryservers_sdk_python import _base, _resource_polling, ips, plans
from cherryservers_sdk_python import regions as regions_module


class BackupStoragePlanModel(_base.ResourceModel):
    """Cherry Server backup storage plan model.

    This model is frozen by default,
    since it represents an actual Cherry Servers backup storage plan.

    Attributes:
        id (int): Plan ID.
        name (str | None): Plan full name.
        slug (str | None): Plan name slug.
        size_gigabytes (int | None): Plan size in GB.
        pricing (list[cherryservers_sdk_python.plans.PricingModel] | None):
         Plan pricing data.
        regions (list[cherryservers_sdk_python.regions.RegionModel] | None):
         Plan region data.
        href (str | None): Plan href.

    """

    id: int = Field(description="Plan ID.")
    name: str | None = Field(description="Plan full name.", default=None)
    slug: str | None = Field(description="Plan name slug.", default=None)
    size_gigabytes: int | None = Field(description="Plan size in GB.", default=None)
    pricing: list[plans.PricingModel] | None = Field(
        description="Plan pricing data.", default=None
    )
    regions: list[regions_module.RegionModel] | None = Field(
        description="Plan region data.", default=None
    )
    href: str | None = Field(description="Plan href.", default=None)


class BackupMethodModel(_base.ResourceModel):
    """Cherry Servers backup method model.

    This model is frozen by default,
    since it represents an actual Cherry Servers backup method.

    Attributes:
        name (str | None): Name of the backup method.
        username (str | None): Username for the backup method.
        password (str | None): Password for the backup method.
        port (int | None): Port for the backup method.
        host (str | None): Host for the backup method.
        ssh_key (str | None): SSH key for the backup method.
        whitelist (list[str] | None): Whitelist for the backup method.
        enabled (bool | None): Whether the backup method is enabled.
        processing (bool | None): Whether the backup method is processing.

    """

    name: str | None = Field(description="Name of the backup method.", default=None)
    username: str | None = Field(
        description="Username for the backup method.", default=None
    )
    password: str | None = Field(
        description="Password for the backup method.", default=None
    )
    port: int | None = Field(description="Port for the backup method.", default=None)
    host: str | None = Field(description="Host for the backup method.", default=None)
    ssh_key: str | None = Field(
        description="SSH key for the backup method.", default=None
    )
    whitelist: list[str] | None = Field(
        description="Whitelist for the backup method.", default=None
    )
    enabled: bool | None = Field(
        description="Whether the backup method is enabled.", default=None
    )
    processing: bool | None = Field(
        description="Whether the backup method is processing.", default=None
    )


class RuleMethodModel(_base.ResourceModel):
    """Cherry Server backup rule method model.

    This model is frozen by default,
    since it represents an actual Cherry Server backup rule method.

    Attributes:
        borg (bool | None): Whether BORG is enabled for the rule.
        ftp (bool | None): Whether FTP is enabled for the rule.
        nfs (bool | None): Whether NFS is enabled for the rule.
        smb (bool | None): Whether SMB is enabled for the rule.

    """

    borg: bool | None = Field(
        description="Whether BORG is enabled for the rule.", default=None
    )
    ftp: bool | None = Field(
        description="Whether FTP is enabled for the rule.", default=None
    )
    nfs: bool | None = Field(
        description="Whether NFS is enabled for the rule.", default=None
    )
    smb: bool | None = Field(
        description="Whether SMB is enabled for the rule.", default=None
    )


class RuleModel(_base.ResourceModel):
    """Cherry Servers backup rule model.

    This model is frozen by default,
    since it represents an actual Cherry Servers backup rule.

    Attributes:
        ip (cherryservers_sdk_python.ips.IPModel | None): Rule IP address.
        methods (RuleMethodModel | None): Rule methods.

    """

    ip: ips.IPModel | None = Field(description="Rule IP address.", default=None)
    methods: RuleMethodModel | None = Field(description="Rule methods.", default=None)


class BackupStorageModel(_base.ResourceModel):
    """Cherry Servers backup storage model.

    This model is frozen by default,
    since it represents an actual Cherry Servers backup storage resource state.

    Attributes:
        id (int): Backup storage ID.
        status (str): Backup storage status.
        state (str | None): Backup storage state.
        private_ip (str | None): Backup storage private IP.
        public_ip (str | None): Backup storage public IP.
        size_gigabytes (int | None): Backup storage total size in GB.
        used_gigabytes (int | None): Backup storage used size in GB.
        attached_to (cherryservers_sdk_python.ips.AttachedServerModel | None):
         The server to which to storage is attached to.
        methods (list[BackupMethodModel] | None): Backup methods.
        available_addresses (list[cherryservers_sdk_python.ips.IPModel] | None):
         Available addresses.
        rules (list[RuleModel] | None): Backup rules.
        plan (cherryservers_sdk_python.plans.PlanModel | None): Backup plan.
        pricing (cherryservers_sdk_python.plans.PricingModel | None): Backup pricing.
        region (cherryservers_sdk_python.regions.RegionModel | None): Backup region.
        href (str | None): Backup href.

    """

    id: int = Field(description="Backup storage ID.")
    status: str = Field(description="Backup storage status.")
    state: str | None = Field(description="Backup storage state.", default=None)
    private_ip: str | None = Field(
        description="Backup storage private IP.", default=None
    )
    public_ip: str | None = Field(description="Backup storage public IP.", default=None)
    size_gigabytes: int | None = Field(
        description="Backup storage total size in GB.", default=None
    )
    used_gigabytes: int | None = Field(
        description="Backup storage used size in GB.", default=None
    )
    attached_to: ips.AttachedServerModel | None = Field(
        description="Server to which the storage is attached to.", default=None
    )
    methods: list[BackupMethodModel] | None = Field(
        description="Backup methods.", default=None
    )
    available_addresses: list[ips.IPModel] | None = Field(
        description="Available addresses.", default=None
    )
    rules: list[RuleModel] | None = Field(description="Backup rules.", default=None)
    plan: plans.PlanModel | None = Field(description="Backup plan.", default=None)
    pricing: plans.PricingModel | None = Field(
        description="Backup pricing.", default=None
    )
    region: regions_module.RegionModel | None = Field(
        description="Backup region.", default=None
    )
    href: str | None = Field(description="Backup href.", default=None)


class CreationRequest(_base.RequestSchema):
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


class UpdateRequest(_base.RequestSchema):
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


class UpdateAccessMethodsRequest(_base.RequestSchema):
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


class BackupStorageClient(_base.ResourceClient):
    """Cherry Servers backup storage client.

    Manage Cherry Servers backup storage resources.
    This class should typically be initialized by

    :class:`cherryservers_sdk_python.facade.CherryApiFacade`.

    Example:
        .. code-block:: python

            facade = cherryservers_sdk_python.facade.CherryApiFacade(token="my-token")

            # Get storage by ID.
            storage = facade.backup_storages.get_by_id(123456)

            # List all project storages.
            for storage in facade.backup_storages.list_by_project(123456):
                print(storage.get_model())

            # List available storage plans.
            for plan_model in facade.backup_storages.list_backup_plans():
                print(plan_model)

            # Create a storage.
            creation_req = cherryservers_sdk_python.backup_storages.CreationRequest(
                region="LT-Siauliai", slug="backup_50"
            )
            storage = facade.backup_storages.create(creation_req, server_id=123456)

            # Update storage.
            update_req = (
                cherryservers_sdk_python.backup_storages.UpdateRequest(slug="backup_500")
            )
            storage.update(update_req)

            # Update storage access method.
            update_access_req = (
                cherryservers_sdk_python.backup_storages.UpdateAccessMethodsRequest(
                    enabled=False,
                )
            )
            storage.update_access_method(update_access_req, "ftp")

            # Delete storage.
            storage.delete()

    """

    def get_by_id(self, storage_id: int) -> BackupStorage:
        """Retrieve a backup storage."""
        response = self._api_client.get(
            f"backup-storages/{storage_id}",
            {
                "fields": "available_addresses,ip,region,project,href,"
                "targeted_to,hostname,id,bgp,status,state,"
                "private_ip,public_ip,size_gigabytes,"
                "used_gigabytes,methods,rules,plan,pricing,name,"
                "whitelist,enabled,processing"
            },
            self.request_timeout,
        )
        storage_model = BackupStorageModel.model_validate(response.json())
        return BackupStorage(self, storage_model)

    def list_by_project(self, project_id: int) -> list[BackupStorage]:
        """Retrieve all backup storages belonging to a project."""
        response = self._api_client.get(
            f"projects/{project_id}/backup-storages",
            {
                "fields": "available_addresses,ip,region,project,"
                "href,targeted_to,hostname,id,bgp,status,state,"
                "private_ip,public_ip,size_gigabytes,used_gigabytes,"
                "methods,rules,plan,pricing,name,"
                "whitelist,enabled,processing"
            },
            self.request_timeout,
        )
        storages: list[BackupStorage] = []
        for value in response.json():
            storage_model = BackupStorageModel.model_validate(value)
            storages.append(BackupStorage(self, storage_model))

        return storages

    def list_backup_plans(self) -> list[BackupStoragePlanModel]:
        """Retrieve available backup storage plans."""
        response = self._api_client.get(
            "backup-storage-plans",
            {"fields": "plan,pricing,href,region"},
            self.request_timeout,
        )
        available_plans: list[BackupStoragePlanModel] = []
        for value in response.json():
            plan_model = BackupStoragePlanModel.model_validate(value)
            available_plans.append(plan_model)

        return available_plans

    def create(
        self,
        creation_schema: CreationRequest,
        server_id: int,
        *,
        wait_for_active: bool = True,
    ) -> BackupStorage:
        """Create a backup storage."""
        response = self._api_client.post(
            f"servers/{server_id}/backup-storages",
            creation_schema,
            None,
            self.request_timeout,
        )
        backup_storage = BackupStorage(
            self, BackupStorageModel.model_validate(response.json())
        )
        if wait_for_active:
            _resource_polling.wait_for_resource_condition(
                backup_storage, 1200, lambda: backup_storage.get_status() == "deployed"
            )
        return self.get_by_id(response.json()["id"])

    def delete(self, storage_id: int) -> None:
        """Delete backup storage.."""
        self._api_client.delete(
            f"backup-storages/{storage_id}", None, self.request_timeout
        )

    def update(
        self,
        storage_id: int,
        update_schema: UpdateRequest,
        *,
        wait_for_active: bool = True,
    ) -> BackupStorage:
        """Update backup storage."""
        response = self._api_client.put(
            f"backup-storages/{storage_id}", update_schema, None, self.request_timeout
        )
        backup_storage = BackupStorage(
            self, BackupStorageModel.model_validate(response.json())
        )
        if wait_for_active:
            _resource_polling.wait_for_resource_condition(
                backup_storage, 1200, lambda: backup_storage.get_status() == "deployed"
            )
        return self.get_by_id(response.json()["id"])

    def update_access_method(
        self,
        storage_id: int,
        method_name: str,
        update_schema: UpdateAccessMethodsRequest,
    ) -> BackupStorage:
        """Update backup storage access method."""
        self._api_client.patch(
            f"backup-storages/{storage_id}/methods/{method_name}",
            update_schema,
            None,
            self.request_timeout,
        )

        return self.get_by_id(storage_id)


class BackupStorage(
    _base.Resource[BackupStorageClient, BackupStorageModel],
    _resource_polling.RefreshableResource,
):
    """Cherry Servers backup storage resource.

    This class represents an existing Cherry Servers resource
    and should only be initialized by :class:`BackupStorageClient`.
    """

    def delete(self) -> None:
        """Delete Cherry Servers backup storage resource."""
        self._client.delete(self._model.id)

    def update(self, update_schema: UpdateRequest) -> None:
        """Update Cherry Servers backup storage resource."""
        updated = self._client.update(self._model.id, update_schema)
        self._model = updated.get_model()

    def update_access_method(
        self,
        update_schema: UpdateAccessMethodsRequest,
        method_name: str,
    ) -> None:
        """Update Cherry Servers backup storage access method."""
        updated = self._client.update_access_method(
            self._model.id, method_name, update_schema
        )
        self._model = updated.get_model()

    def refresh(self) -> None:
        """Refresh the resource."""
        self._model = self._client.get_by_id(self._model.id).get_model()

    def get_status(self) -> str:
        """Get backup storage status."""
        return self._model.status

    def get_id(self) -> int:
        """Get resource ID."""
        return self._model.id

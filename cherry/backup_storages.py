"""Cherry Servers backup storage resource management module."""

from __future__ import annotations

from pydantic import Field

from cherry import _base, ips, plans
from cherry import regions as regions_module


class BackupStoragePlanModel(_base.ResourceModel):
    """Cherry Server backup storage plan model.

    This model is frozen by default,
    since it represents an actual Cherry Servers backup storage plan.

    Attributes:
        id (int): Plan ID.
        name (str): Plan full name.
        slug (str): Plan name slug.
        size_gigabytes (int): Plan size in GB.
        pricing (list[cherry.plans.PricingModel]): Plan pricing data.
        regions (list[cherry.regions.RegionModel]): Plan region data.
        href (str): Plan href.

    """

    id: int = Field(description="Plan ID.")
    name: str = Field(description="Plan full name.")
    slug: str = Field(description="Plan name slug.")
    size_gigabytes: int = Field(description="Plan size in GB.")
    pricing: list[plans.PricingModel] = Field(description="Plan pricing data.")
    regions: list[regions_module.RegionModel] = Field(description="Plan region data.")
    href: str = Field(description="Plan href.")


class BackupMethodModel(_base.ResourceModel):
    """Cherry Servers backup method model.

    This model is frozen by default,
    since it represents an actual Cherry Servers backup method.

    Attributes:
        name (str): Name of the backup method.
        username (str | None): Username for the backup method.
        password (str | None): Password for the backup method.
        port (int | None): Port for the backup method.
        host (str | None): Host for the backup method.
        ssh_key (str | None): SSH key for the backup method.
        whitelist (list[str]): Whitelist for the backup method.
        enabled (bool): Whether the backup method is enabled.
        processing (bool): Whether the backup method is processing.

    """

    name: str = Field(description="Name of the backup method.")
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
    whitelist: list[str] = Field(description="Whitelist for the backup method.")
    enabled: bool = Field(description="Whether the backup method is enabled.")
    processing: bool = Field(description="Whether the backup method is processing.")


class RuleMethodModel(_base.ResourceModel):
    """Cherry Server backup rule method model.

    This model is frozen by default,
    since it represents an actual Cherry Server backup rule method.

    Attributes:
        borg (bool): Whether BORG is enabled for the rule.
        ftp (bool): Whether FTP is enabled for the rule.
        nfs (bool): Whether NFS is enabled for the rule.
        smb (bool): Whether SMB is enabled for the rule.

    """

    borg: bool = Field(description="Whether BORG is enabled for the rule.")
    ftp: bool = Field(description="Whether FTP is enabled for the rule.")
    nfs: bool = Field(description="Whether NFS is enabled for the rule.")
    smb: bool = Field(description="Whether SMB is enabled for the rule.")


class RuleModel(_base.ResourceModel):
    """Cherry Servers backup rule model.

    This model is frozen by default,
    since it represents an actual Cherry Servers backup rule.

    Attributes:
        ip (cherry.ips.IPModel): Rule IP address.
        methods (RuleMethodModel): Rule methods.

    """

    ip: ips.IPModel = Field(description="Rule IP address.")
    methods: RuleMethodModel = Field(description="Rule methods.")


class BackupStorageModel(_base.ResourceModel):
    """Cherry Servers backup storage model.

    This model is frozen by default,
    since it represents an actual Cherry Servers backup storage resource state.

    Attributes:
        id (int): Backup storage ID.
        status (str): Backup storage status.
        state (str): Backup storage state.
        private_ip (str | None): Backup storage private IP.
        public_ip (str | None): Backup storage public IP.
        size_gigabytes (int): Backup storage total size in GB.
        used_gigabytes (int): Backup storage used size in GB.
         attached_to (cherry.servers.AttachedServerModel | None):
        The server to which to storage is attached to.
        methods (list[BackupMethodModel]): Backup methods.
        available_addresses (list[cherry.ips.IPModel]): Available addresses.
        rules (list[RuleModel]): Backup rules.
        plan (cherry.plans.PlanModel): Backup plan.
        pricing (cherry.plans.PricingModel): Backup pricing.
        region (cherry.regions.RegionModel): Backup region.
        href (str): Backup href.

    """

    id: int = Field(description="Backup storage ID.")
    status: str = Field(description="Backup storage status.")
    state: str = Field(description="Backup storage state.")
    private_ip: str | None = Field(
        description="Backup storage private IP.", default=None
    )
    public_ip: str | None = Field(description="Backup storage public IP.", default=None)
    size_gigabytes: int = Field(description="Backup storage total size in GB.")
    used_gigabytes: int = Field(description="Backup storage used size in GB.")
    attached_to: ips.AttachedServerModel | None = Field(
        description="Server to which the storage is attached to.", default=None
    )
    methods: list[BackupMethodModel] = Field(description="Backup methods.")
    available_addresses: list[ips.IPModel] = Field(description="Available addresses.")
    rules: list[RuleModel] = Field(description="Backup rules.")
    plan: plans.PlanModel = Field(description="Backup plan.")
    pricing: plans.PricingModel = Field(description="Backup pricing.")
    region: regions_module.RegionModel = Field(description="Backup region.")
    href: str = Field(description="Backup href.")


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

    :class:`cherry.facade.CherryApiFacade`.

    Example:
        .. code-block:: python

            facade = cherry.facade.CherryApiFacade(token="my-token")

            # Get storage by ID.
            storage = facade.backup_storages.get_by_id(123456)

            # List all project storages.
            print("List of all project storages:")
            for storage in facade.backup_storages.list_by_project(123456):
                print(storage.model)
            print("______________________________")

            # List available storage plans.
            print("List of available backup storage plans:")
            for plan_model in facade.backup_storages.list_backup_plans():
                print(plan_model)
            print("______________________________")

            # Create a storage.
            creation_req = cherry.backup_storages.CreationRequest(
                region="eu_nord_1", slug="backup_50"
            )
            storage = facade.backup_storages.create(creation_req, server_id=123456)

            # Update storage.
            update_req = (
                cherry.backup_storages.UpdateRequest(slug="backup_500")
            )
            storage.update(update_req)

            # Update storage access method.
            update_access_req = (
                cherry.backup_storages.UpdateAccessMethodsRequest(
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
            10,
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
            10,
        )
        storages: list[BackupStorage] = []
        for value in response.json():
            storage_model = BackupStorageModel.model_validate(value)
            storages.append(BackupStorage(self, storage_model))

        return storages

    def list_backup_plans(self) -> list[BackupStoragePlanModel]:
        """Retrieve available backup storage plans."""
        response = self._api_client.get(
            "backup-storage-plans", {"fields": "plan,pricing,href,region"}, 20
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
    ) -> BackupStorage:
        """Create a backup storage."""
        response = self._api_client.post(
            f"servers/{server_id}/backup-storages", creation_schema, None, 30
        )
        return self.get_by_id(response.json()["id"])

    def delete(self, storage_id: int) -> None:
        """Delete backup storage.."""
        self._api_client.delete(f"backup-storages/{storage_id}", None, 10)

    def update(
        self,
        storage_id: int,
        update_schema: UpdateRequest,
    ) -> BackupStorage:
        """Update backup storage."""
        response = self._api_client.put(
            f"backup-storages/{storage_id}", update_schema, None, 30
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
            20,
        )

        return self.get_by_id(storage_id)


class BackupStorage(_base.Resource[BackupStorageClient, BackupStorageModel]):
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
        self._model = updated.get_model_copy()

    def update_access_method(
        self,
        update_schema: UpdateAccessMethodsRequest,
        method_name: str,
    ) -> None:
        """Update Cherry Servers backup storage access method."""
        updated = self._client.update_access_method(
            self._model.id, method_name, update_schema
        )
        self._model = updated.get_model_copy()

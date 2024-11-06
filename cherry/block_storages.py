"""Cherry Servers EBS resource management module."""

from __future__ import annotations

from pydantic import Field

from cherry import _client, _models, request_schemas
from cherry.ips import AttachedServerModel
from cherry.regions import RegionModel


class BlockStorageModel(_models.DefaultModel):
    """Cherry Servers Elastic Block Storage model.

    This model is frozen by default,
    since it represents an actual Cherry Servers EBS resource state.

    Attributes:
        id (int): EBS ID.
        name (str): EBS name.
        href (str): EBS href.
        size (int): EBS size.
        allow_edit_size (bool): Whether size can be edited.
        unit (str): Size measurement unit.
        attached_to (cherry.ips.AttachedServerModel | None):
         EBS attached server data.
        vlan_id (str | None): EBS VLAN ID.
        vlan_ip (str | None): EBS VLAN IP address.
        initiator (str | None): EBS initiator.
        discovery_ip (str | None): EBS discovery IP address.
        region (cherry.regions.RegionModel): Region data.

    """

    id: int = Field(description="EBS ID.")
    name: str = Field(description="EBS name.")
    href: str = Field(description="EBS href.")
    size: int = Field(description="EBS size.")
    allow_edit_size: bool = Field(description="Whether size can be edited.")
    unit: str = Field(description="Size measurement unit.")
    attached_to: AttachedServerModel | None = Field(
        description="EBS attached server model.", default=None
    )
    vlan_id: str | None = Field(description="EBS VLAN ID.", default=None)
    vlan_ip: str | None = Field(description="EBS VLAN IP address.", default=None)
    initiator: str | None = Field(description="EBS initiator.", default=None)
    discovery_ip: str | None = Field(
        description="EBS discovery IP address.", default=None
    )
    region: RegionModel = Field(description="Region data.")


class BlockStorage:
    """Cherry Servers block storage resource.

    This class represents an existing Cherry Servers resource
    and should only be initialized by :class:`BlockStorageClient`.

    Attributes:
        model (BlockStorageModel): Cherry Servers elastic block storage model.
            This is a Pydantic model that contains block storage data.
            A standard dictionary can be extracted with ``model.model_dump()``.

    """

    def __init__(self, client: BlockStorageClient, model: BlockStorageModel) -> None:
        """Initialize a Cherry Servers block storage resource."""
        self._client = client
        self.model = model

    def delete(self) -> None:
        """Delete Cherry Servers block storage resource."""
        self._client.delete(self.model.id)

    def update(
        self, update_schema: request_schemas.block_storages.UpdateRequest
    ) -> None:
        """Update Cherry Servers block storage resource.

        WARNING: increasing storage size will generate a new block storage ID
        and make the old one invalid, making this resource obsolete.
        You will then need to create a new instance of :class:`BlockStorage`
        to perform further operations.
        """
        self._client.update(self.model.id, update_schema)

    def attach(
        self, attach_schema: request_schemas.block_storages.AttachRequest
    ) -> None:
        """Attach Cherry Servers block storage resource to server.

        Block storage volumes can only be attached to baremetal servers.
        """
        attached = self._client.attach(self.model.id, attach_schema)
        self.model = attached.model

    def detach(self) -> None:
        """Detach Cherry Servers block storage resource from server."""
        detached = self._client.detach(self.model.id)
        self.model = detached.model


class BlockStorageClient:
    """Cherry Servers block storage client.

    Manage Cherry Servers block storage resources.
    This class should typically be initialized by
    :class:`cherry.facade.CherryApiFacade`.

    Example:
        .. code-block:: python

            # Get storage by ID.
            storage = facade.block_storages.get_by_id(123456)

            # List all project storages.
            print("List of all project storages:")
            for storage in facade.block_storages.list_by_project(123456):
                print(storage.model)

            # Create a storage.
            creation_req = cherry.request_schemas.block_storages.CreationRequest(
                region="eu_nord_1", size=1
            )
            storage = facade.block_storages.create(creation_req, project_id=123456)

            # Update storage.
            update_req = cherry.request_schemas.block_storages.UpdateRequest(
                description="updated", size=2
            )
            storage.update(update_req)

            # Attach storage.
            attach_req = cherry.request_schemas.block_storages.AttachRequest(
                attach_to=123456
            )
            storage.attach(attach_req)

            # Detach storage.
            storage.detach()

            # Delete storage.
            storage.delete()

    """

    def __init__(self, api_client: _client.CherryApiClient) -> None:
        """Initialize a Cherry Servers block storage client."""
        self._api_client = api_client

    def get_by_id(self, storage_id: int) -> BlockStorage:
        """Retrieve a block storage by ID."""
        response = self._api_client.get(
            f"storages/{storage_id}",
            None,
            10,
        )
        storage_model = BlockStorageModel.model_validate(response.json())
        return BlockStorage(self, storage_model)

    def list_by_project(self, project_id: int) -> list[BlockStorage]:
        """Retrieve all block storages that belong to a specified project."""
        response = self._api_client.get(
            f"projects/{project_id}/storages",
            None,
            10,
        )
        storages: list[BlockStorage] = []
        for value in response.json():
            storage_model = BlockStorageModel.model_validate(value)
            storages.append(BlockStorage(self, storage_model))

        return storages

    def create(
        self,
        creation_schema: request_schemas.block_storages.CreationRequest,
        project_id: int,
    ) -> BlockStorage:
        """Create a new block storage."""
        response = self._api_client.post(
            f"projects/{project_id}/storages", creation_schema, None, 30
        )
        return self.get_by_id(response.json()["id"])

    def delete(self, storage_id: int) -> None:
        """Delete block storage."""
        self._api_client.delete(f"storages/{storage_id}", None, 10)

    def update(
        self,
        storage_id: int,
        update_schema: request_schemas.block_storages.UpdateRequest,
    ) -> None:
        """Update block storage.

        Increasing storage size will generate a new block storage ID
        and make the old one invalid.
        """
        self._api_client.put(f"storages/{storage_id}", update_schema, None, 30)

    def attach(
        self,
        storage_id: int,
        attach_schema: request_schemas.block_storages.AttachRequest,
    ) -> BlockStorage:
        """Attach block storage to server."""
        response = self._api_client.post(
            f"storages/{storage_id}/attachments", attach_schema, None, 30
        )

        return self.get_by_id(response.json()["id"])

    def detach(self, storage_id: int) -> BlockStorage:
        """Detach block storage from server."""
        self._api_client.delete(f"storages/{storage_id}/attachments", None, 10)

        return self.get_by_id(storage_id)
